import matplotlib.pyplot as plt
import numpy as np

# se référer à l'exercice 17-01 d'analyse B

x_t1 = lambda t: 3*t - t**3
x_t2 = lambda t: -3*t**2 + 3

y_t1 = lambda t: 1 - t**2
y_t2 = lambda t: -2*t

t1_range = np.linspace(-2, 2, 1000)
t2_range = np.linspace(-2, 2, 75)

### plot

fig = plt.figure()

plt.plot(x_t1(t1_range), y_t1(t1_range), color='blue')
# plt.plot(x_t2(t1_range), y_t2(t1_range), color='red')

for i in t2_range:
	start_point = (x_t1(i), y_t1(i))
	end_point = (start_point[0] + x_t2(i), start_point[1] + y_t2(i))
	plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], color='gray', linestyle='-', linewidth=0.5)

plt.grid()
plt.show()

fig.savefig('graph.png')
