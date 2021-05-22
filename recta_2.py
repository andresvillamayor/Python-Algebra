#  mostrar una recta en un plano cartesiano
#  usaremos el scatter
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-15,15)
y = 2 * x + 3

plt.axhline(0, color='black')
plt.axvline(0, color='black')

#  agregramos los datos de x en el grafico
plt.scatter(x, y)
plt.show()
