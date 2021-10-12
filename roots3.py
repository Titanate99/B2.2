#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:45:26 2021

@author: nate_mac
"""


"""
plot_function.py
Plots the function cos(x) - exp(-x).
"""

# Import needed modules
from pylab import *

from scipy.optimize import fsolve

def func(x):
    return cos(x) - exp(-x)

def func2(x):
    return x * (e**(x)) /(e**(x)- 1) - 5

print(fsolve(func,0))



x = fsolve(func2,5)




print(func2(1))

