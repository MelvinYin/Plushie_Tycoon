import numpy as np
import matplotlib.pyplot as plt

np.random.seed(40)
import math

x = np.random.normal(0, 1, 100)
print(sum(x))

damping = 0.02
y = []
value = 0
for i, val in enumerate(x):
    value += val
    value -= damping * (value ** 2) * np.sign(value)
    y.append(value)

plt.figure(0)
plt.plot(y, "x-")

x = y.copy()
y = []
value = 0
for i, val in enumerate(x):
    value += val
    value -= damping * (value ** 2) * np.sign(value)
    y.append(value)

final = y

plt.figure(1)
plt.plot(final, "x-")
plt.show()