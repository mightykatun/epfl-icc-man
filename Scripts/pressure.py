import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Set plotting parameters
mpl.rcParams["lines.linewidth"] = 0.8
plt.rcParams["figure.autolayout"] = True
ratio = 0.75
width = 5
dpi = 750
form = "png"

# Fluid properties (densities in kg/m^3)
rho_huile = 0.84  # density of oil
rho_eau = 1       # density of water
air_p = 101325        # atmospheric pressure (Pa)
g = 9.81

npoints = 10000  # number of vertical steps

# Create an array for depths from 0 (surface) to -2 m (bottom)
depths = np.linspace(0, -2, npoints)

# Initialize the pressure profile array
pressure = np.empty_like(depths)

# Calculate pressure for each depth:
# If z is between 0 and -1 m, the column is oil only.
# If z is below -1 m, then the column consists of a 1 m oil layer plus a water layer.
for i, z in enumerate(depths):
    if z >= -1:
        # In the oil layer: depth (0 to 1 m oil) is -z (since z is negative)
        pressure[i] = air_p + rho_huile * g * (-z)
    else:
        # In the water layer: add full oil contribution (for 1 m) then the extra water depth
        pressure[i] = air_p + rho_huile * g * 1 + rho_eau * g * (-(z + 1))

# Create a horizontal x-axis from 0 to 1 m
x = np.linspace(0, 1, npoints)
# Create a 2D grid for plotting. The pressure profile is replicated in the x-direction.
X, Y = np.meshgrid(x, depths)
P = np.tile(pressure.reshape(-1, 1), (1, npoints))

# Plot the pressure distribution
fig, ax = plt.subplots(figsize=(width, width*ratio))
# Using 'extent' sets the axes to show x from 0 to 1 and depth from -2 to 0
c = ax.imshow(P, cmap='Blues', interpolation='nearest', extent=[0, 1, -2, 0], aspect='auto')
ax.set_xlabel("x (m)")
ax.set_ylabel("Depth (m)")
ax.set_title("Pressure Distribution in Container")
fig.colorbar(c, ax=ax, label="Pressure (Pa)")
ax.grid(True)
plt.show()
