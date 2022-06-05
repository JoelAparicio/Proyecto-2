import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

fx = lambda x: x ** 3 - 2 * x - 5
dfx = lambda x: 3 * (x ** 2) + 2


def f(x):
    return (x ** 3 - 2 * x - 5)


resultado = optimize.newton(f, 1.5)

x0 = 2
tolera = 0.001

tabla = []
tramo = abs(2 * tolera)
xi = x0
while (tramo >= tolera):
    xnuevo = xi - fx(xi) / dfx(xi)
    tramo = abs(xnuevo - xi)
    tabla.append([xi, xnuevo, tramo])
    xi = xnuevo

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision=4)
print(tabla)
print('La raiz es: {}'.format(resultado))
print('con error de: ', tramo)

x = np.linspace(-100, 100)

xx = fx(x)
plt.plot(x, xx)
plt.show()
