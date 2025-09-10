#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%% [markdown]

import matplotlib.pyplot as plt
import numpy as np
import os
import sys

x0 = float(input("Enter initial position (m): "))
v0 = float(input("Enter initial velocity (m/s): "))
a = float(input("Enter acceleration (m/s^2): "))


t = np.linspace(0, 10, num=100)
v = v0 + a*t
x = x0 + v0*t + 0.5*a*t**2



fig, axs = plt.subplots(3, 1, figsize=(8, 12))

axs[0].plot(t, x)
axs[0].set_title("Position vs Time")
axs[0].set_ylabel("Position (m)")
axs[0].grid()

axs[1].plot(t, v)
axs[1].set_title("Velocity vs Time")
axs[1].set_ylabel("Velocity (m/s)")
axs[1].grid()

axs[2].plot(t, np.full_like(t, a))
axs[2].set_title("Acceleration vs Time")
axs[2].set_xlabel("Time (s)")
axs[2].set_ylabel("Acceleration (m/s²)")
axs[2].grid()

plt.show()


