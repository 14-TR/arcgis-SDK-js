import xarray as xr

# Define the path to your extracted Zarr dataset
zarr_path = r"C:\Users\TR\Downloads\gistemp1200_GHCNv4_ERSSTv5.zarr"  # Use raw string


# Open the dataset
ds = xr.open_zarr(zarr_path)

# Inspect the dataset
print(ds)
