import matplotlib.pyplot as plt
import numpy as np

# constants
e_0 = 8.85e-12
e = 1.602e-19


field = lambda x, y, coor: 1 / (4 * np.pi * e_0) * coor[2] / np.exp((x-coor[0])**2 + (y-coor[1])**2) # assuming particle is centered on coor, taking the exponential of the distance to not jump to infty
# note that this is not the force felt by a second particle of arbitrary charge Q, this is the electrical field E

array = np.linspace(-5, 5, 100)

# list of particles that influence the field
p_list = [
	(0, 0, e),
	(2, 3, 2*e),
	(0, 1.5, -e),
	(-3, -3, -4*e)
	]

x, y = np.meshgrid(array, array)
z = sum([field(x, y, coor) for coor in p_list])

# the plot shows the combined effect of all those particles on a virtual particle of charge e, at every point of the grid
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
plt.savefig('charges.png', transparent=True)
plt.show()
