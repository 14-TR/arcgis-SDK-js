import tarfile
import os

tar_path = r"C:/Users/TR/Downloads/gistemp1200_GHCNv4_ERSSTv5.zarr.tar.gz"
extract_path = r"C:/Users/TR/Downloads/gistemp1200_GHCNv4_ERSSTv5.zarr"

# Extract the archive
if not os.path.exists(extract_path):
    print(f"Extracting {tar_path}...")
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=extract_path)
    print(f"Extracted to {extract_path}")
else:
    print(f"Archive already extracted at {extract_path}")
