import xarray as xr
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os
import tarfile

# Set input and output paths here
INPUT_PATH = r"C:/Users/TR/Downloads/gistemp1200_GHCNv4_ERSSTv5.zarr.tar"
EXTRACT_PATH = r"C:/Users/TR/Desktop/GIT/arcgis-SDK-js/backend/data/raw/gistemp.zarr"
OUTPUT_PATH = r"C:/Users/TR/Desktop/GIT/arcgis-SDK-js/backend/data/temperature_anomalies.geojson"
PRECISION = 3  # Decimal precision for latitude/longitude (adjust if needed)

os.makedirs(EXTRACT_PATH, exist_ok=True)

print("Extracting Zarr archive...")
with tarfile.open(INPUT_PATH, "r:gz") as tar:
    tar.extractall(path=EXTRACT_PATH)
print(f"Archive extracted to: {EXTRACT_PATH}")

def process_zarr_to_geojson(input_path, output_path, precision=2):
    """
    Process a Zarr file containing temperature anomalies and export as GeoJSON.

    Parameters:
        input_path (str): Path to the Zarr dataset.
        output_path (str): Path to save the output GeoJSON file.
        precision (int): Decimal precision for latitude/longitude.
    """
    print("Loading Zarr dataset...")
    # Load the Zarr dataset
    ds = xr.open_zarr(input_path)

    # Inspect the dataset to identify variable names
    print("Dataset variables:", ds.variables)

    # Adjust the variable name as per the dataset
    # Replace 'temperature_anomaly' with the correct variable name in your Zarr file
    try:
        temp_data = ds["temperature_anomaly"]  # Adjust the variable name
    except KeyError:
        print("Error: 'temperature_anomaly' variable not found in the dataset.")
        print(f"Available variables: {list(ds.variables)}")
        return

    # Flatten the data into a Pandas DataFrame
    print("Flattening the dataset...")
    df = temp_data.to_dataframe().reset_index()

    # Filter and clean data
    print("Cleaning data...")
    df = df[['lat', 'lon', 'temperature_anomaly']].dropna()
    df = df.rename(columns={'lat': 'Latitude', 'lon': 'Longitude', 'temperature_anomaly': 'Anomaly'})

    # Reduce precision to optimize GeoJSON size
    print(f"Reducing precision to {precision} decimals...")
    df['Latitude'] = df['Latitude'].round(precision)
    df['Longitude'] = df['Longitude'].round(precision)

    # Convert to GeoDataFrame with Point geometries
    print("Creating GeoDataFrame...")
    df['geometry'] = df.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
    gdf = gpd.GeoDataFrame(df, geometry='geometry')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Export to GeoJSON
    print(f"Saving to {output_path}...")
    gdf.to_file(output_path, driver='GeoJSON')

    print("Processing complete. GeoJSON file saved.")

if __name__ == "__main__":
    # Process Zarr to GeoJSON using the hardcoded paths
    process_zarr_to_geojson(INPUT_PATH, OUTPUT_PATH, PRECISION)
