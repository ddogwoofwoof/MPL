# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:07:54 2019

@author: Asus
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

import numpy as np

np.random.seed(1000)

y = np.random.standard_normal((1000,2))

plt.figure(figsize=(10,6))
plt.plot(y[:, 0], y[:, 1], 'ro')
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot');