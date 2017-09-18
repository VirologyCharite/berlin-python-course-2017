#!/usr/bin/env python

import matplotlib.pyplot as plt
from random import uniform

x = [uniform(0, 100) for _ in range(100)]

# Equivalently:
# x = []
# for _ in range(100):
#     x.append(uniform(0, 100))

# plt.hist(x, bins=7)
plt.hist(x, bins=7, rwidth=0.95, log=True, color='red')

plt.savefig('output.png')
# plt.show()
