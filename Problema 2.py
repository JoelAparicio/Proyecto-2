import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(x):
    return (x ** 3 - 2 * x - 5)
resultado = optimize.newton(f, 1.5)

fx = lambda x: x ** 3 - 2 * x - 5
dfx = lambda x: 3 * (x ** 2) + 2
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

#Convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

#Salida
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision=4)
print(tabla)
print('La raiz es: {}'.format(resultado))
print('con error de: ', tramo)

#Se grafica el metodo
x = np.linspace(-15, 15, 1000)
xx = fx(x)
plt.plot(x, xx)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.show()
