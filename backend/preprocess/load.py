import xarray as xr

zarr_path = r"C:/Users/TR/Downloads/gistemp1200_GHCNv4_ERSSTv5.zarr/gistemp1200_GHCNv4_ERSSTv5.zarr"


try:
    # Attempt to open the Zarr dataset
    ds = xr.open_zarr(zarr_path)
    print("Dataset successfully loaded!")
    print(ds)
except Exception as e:
    print(f"Error loading dataset: {e}")
