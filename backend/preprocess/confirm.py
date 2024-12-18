import os

zarr_path = r"C:/Users/TR/Downloads/gistemp1200_GHCNv4_ERSSTv5.zarr"

# Walk through the extracted directory
print(f"Contents of {zarr_path}:")
for root, dirs, files in os.walk(zarr_path):
    level = root.replace(zarr_path, "").count(os.sep)
    indent = " " * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = " " * 4 * (level + 1)
    for f in files:
        print(f"{sub_indent}{f}")
