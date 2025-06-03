import matplotlib.pyplot as plt
import numpy as np

# Constants
mu_0 = 4e-7 * np.pi
I = 1

coeff = (mu_0 * I) / (2 * np.pi)
axis = np.linspace(-1, 1, 8)

x, y, z = np.meshgrid(axis, axis, np.linspace(-1, 1, 3))
r = np.sqrt(x**2 + y**2)

# Calculate the magnetic field components
Bx = -y / r * coeff
By = x / r * coeff

c = coeff / r
c = (c.ravel() - c.min()) / np.ptp(c)
c = plt.cm.viridis(c)

ax = plt.axes(projection='3d')
quiver = ax.quiver(x, y, z, Bx, By, np.zeros_like(x), colors=c, length=0.2, normalize=True)
plt.plot((0, 0), (0, 0), (-2, 2), color="black")
plt.savefig('lorentz.png')
plt.show()
