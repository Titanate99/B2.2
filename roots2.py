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

# Define the function
def func(x):
    return x * (e**(x)) /(e**(x)- 1) - 5

# Create an x-axis and function array
x = linspace(4,6,100)
y = func(x)

# Plot the result
figure(1)      # define the figure window to use
clf()          # clear the current figure window
plot(x,y,'r-')
xlabel('x')
ylabel('cos(x) - exp(-x)')

# Plot the x-axis to make the zeros easy to find
plot(x,zeros(100),'k-')