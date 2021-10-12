#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:31:14 2021

@author: nate_mac
"""
import numpy as np

from pylab import *

from scipy.optimize import fsolve

me = 9.11e-31 #kg
a = 0.529e-10 #m
V_0 = 1000 *(1.602e-19) #keV
h_bar = (6.626e-34)/2 * np.pi #J * Hz-1

k = (2 * me * (a**2) * V_0 / (h_bar)**2 )** (1/2) 

print(k) 

def func(s):
    return -((k**2)-(s**2))**(1/2) / s * (np.cos(s)/np.sin(s))

s = fsolve(func,2)

print(s)

E = V_0 * (1-(s**2/k**2))

print(int(E))






