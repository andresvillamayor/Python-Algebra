
#  Ecuacion de la recta
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-15,15)
y = 2 * x + 3

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.plot(x, y)
plt.show()
