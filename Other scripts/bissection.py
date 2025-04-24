#!/usr/bin/env python

'''
Computes a root of a function in a given interval with the bissection method
'''

import numpy as np
from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify


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

def bissection(lower, upper):
    if f(lower) < 0 and f(upper) > 0:
        middle = (lower + upper) / 2
        if f(middle) >= 0:
            new_interval = (lower, middle)
        elif f(middle) < 0:
            new_interval = (middle, upper)

    elif f(lower) > 0 and f(upper) < 0:
        middle = (lower + upper) / 2
        if f(middle) >= 0:
            new_interval = (middle, upper)
        elif f(middle) < 0:
            new_interval = (lower, middle)
    
    else:
        print(error1)
        exit()
    
    print(f'New interval is {new_interval}')
    return new_interval
        

if f(mini) == 0:
    print('The lower bound is a root')
if f(maxi) == 0:
    print('The upper bound is a root')

else:
    for i in range(iterations):
        mini, maxi = bissection(mini, maxi)

    s = ((mini + maxi) / 2)
    print()
    print(f'Root approx. {s}, f({s})={f(s)}')
