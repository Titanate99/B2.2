#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:45:26 2021

@author: nate_mac
"""
import matplotlib.pyplot as plt

import numpy as np


x = np.linspace(-2,2,100) # create x array
lhs = np.exp(-x)          # create lhs array
rhs = np.cos(x)           # create rhs array
plt.plot(x,rhs,'r-')       # plot lhs as solid red curve
plt.plot(x,lhs,'b--')      # plot rhs as dashed blue curve