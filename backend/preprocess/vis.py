import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.animation import FuncAnimation

# Load the dataset
zarr_path = r"C:/Users/TR/Downloads/gistemp1200_GHCNv4_ERSSTv5.zarr/gistemp1200_GHCNv4_ERSSTv5.zarr"
ds = xr.open_zarr(zarr_path)

# Extract the temperature anomaly variable
temp_anomaly = ds["tempanomaly"]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={"projection": ccrs.PlateCarree()})
ax.coastlines()

# Initial plot (first frame)
img = ax.imshow(
    temp_anomaly.isel(time=0).values,
    extent=[
        ds["lon"].values.min(),
        ds["lon"].values.max(),
        ds["lat"].values.min(),
        ds["lat"].values.max()
    ],
    transform=ccrs.PlateCarree(),
    cmap="coolwarm",
    origin="upper",
    vmin=-5,  # Adjust based on anomaly range
    vmax=5    # Adjust based on anomaly range
)
cbar = plt.colorbar(img, ax=ax, orientation="vertical", label="Temperature Anomaly (°C)")
title = ax.set_title("Global Temperature Anomaly")

# Update function for animation
def update(frame):
    img.set_data(temp_anomaly.isel(time=frame).values)
    title.set_text(f"Global Temperature Anomaly - {str(temp_anomaly['time'].values[frame])[:10]}")
    return [img, title]

# Animate over all time steps
ani = FuncAnimation(fig, update, frames=len(temp_anomaly["time"]), interval=100)

# Save the animation (optional)
ani.save("temperature_anomaly_animation.gif", writer="pillow", fps=10)

plt.show()
