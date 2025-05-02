#!/usr/bin/env python

'''
Computes a root of a function in a given interval with the bissection method, updating plots using matplotlib
'''

import numpy as np
from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt

# expr = input('Continuous function to evaluate: ')
# mini = int(input('Lower bound for x: '))
# maxi = int(input('Upper bound for x: '))x**3-4*x-9

expr = 'x**15-7'
mini = 1
maxi = 2

iterations = 50

error1 = '''The interval has no sign change, could be a float error,
try changing the start interval or lowering the amount of iterations'''

x = var('x')
expr = sympify(expr)
f = lambdify(x, expr)

def plot_interval(lower, upper):
    x_vals = np.linspace(lower, upper, 400)
    y_vals = f(x_vals)
    
    # plt.clf()  # Clear the previous figure
    plt.plot(x_vals, y_vals, label='Function')
    plt.axhline(0, color='black', linewidth=0.5)  # X-axis
    plt.title('Bissection Method Progress')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.scatter([lower], [f(lower)], color='red', label='Lower bound')
    plt.scatter([upper], [f(upper)], color='blue', label='Upper bound')
    plt.legend()
    plt.pause(0.05)  # Pause for a short time to update the plot

def bissection(lower, upper):
    if f(lower) * f(upper) >= 0:
        print("Error: The function has the same sign at both endpoints.")
        return lower, upper
    
    middle = (lower + upper) / 2
    plot_interval(lower, upper)  # Update plot with current interval

    if f(middle) == 0:
        print('Root found exactly at:', middle)
        return lower, middle
    elif f(lower) * f(middle) < 0:
        return lower, middle
    else:
        return middle, upper

if __name__ == "__main__":
    plot_interval(mini, maxi)  # Initial plot of the starting interval
    
    for i in range(iterations):
        mini, maxi = bissection(mini, maxi)

    s = (mini + maxi) / 2
    print()
    print(f'Root approx. {s}, f({s})={f(s)}')