import xarray as xr
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import numpy as np
import os

# Load the Zarr dataset
zarr_path = r"C:/Users/TR/Downloads/gistemp1200_GHCNv4_ERSSTv5.zarr/gistemp1200_GHCNv4_ERSSTv5.zarr"
ds = xr.open_zarr(zarr_path)

# Create output directory for GeoJSON files
output_dir = "backend\data\temperature_anomalies_geojson"
os.makedirs(output_dir, exist_ok=True)

# Get the unique years from the dataset
years = pd.to_datetime(ds["time"].values).year.unique()

# Iterate through each year and create a GeoJSON
for year in years:
    print(f"Processing year: {year}")
    
    # Extract mean temperature anomaly for the year
    yearly_anomaly = ds["tempanomaly"].sel(time=str(year)).mean(dim="time")
    
    # Flatten lat/lon grid into a DataFrame
    lat, lon = ds["lat"].values, ds["lon"].values
    lon_grid, lat_grid = np.meshgrid(lon, lat)  # Use numpy for meshgrid
    df = pd.DataFrame({
        "Latitude": lat_grid.ravel(),
        "Longitude": lon_grid.ravel(),
        "Anomaly": yearly_anomaly.values.ravel()
    }).dropna()

    # Convert to GeoDataFrame with CRS
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df["Longitude"], df["Latitude"]),
        crs="EPSG:4326"  # Define CRS as WGS 84
    )

    # Export to GeoJSON
    output_path = os.path.join(output_dir, f"temperature_anomalies_{year}.geojson")
    gdf.to_file(output_path, driver="GeoJSON")
    print(f"Saved GeoJSON for {year}: {output_path}")

print("All years processed!")
