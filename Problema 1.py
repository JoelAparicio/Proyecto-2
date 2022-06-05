from matplotlib import pyplot


def regula_falsi(funcion, x_a, x_b, iteraciones=10, error_r=0.01):
    # Se inicializan las variables
    solucion = None
    contador = 0
    error_calculado = 100
    # Se evalua si la raiz esta dentro del intervalo
    if funcion(x_a) * funcion(x_b) <= 0:
        # Se procede a calcular la funcion
        while contador <= iteraciones and error_calculado >= error_r:
            contador += 1
            solucion = x_b - ((funcion(x_b) * (x_b - x_a)) / (funcion(x_b) - funcion(x_a)))
            error_calculado = abs((solucion - x_a) / solucion) * 100
            # Se redefine el nuevo intervalo con los signos
            if funcion(x_a) * funcion(solucion) >= 0:  # Si la funcion evaluada en el punto a por la funcion evaluada
                # en la solucion es mayor o igual a 0
                x_a = solucion
            else:
                x_b = solucion

        print('X resultante: {:.4f}'.format(solucion))
        print('Numero de iteraciones: {:.0f}'.format(contador) + ' iteraciones')
        print('Error relativo: {:.4f}'.format(error_calculado) + '%')
    else:
        print('no existe solucion en ese intervalo propuesto')


# Función cuadrática.
def f1(x):
    return -0.5 * (x ** 2) + 2.5 * x + 4.5


# Función lineal que corta la funcion cuadratica.
def f2(x):
    return 2 * x + 0


# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-15, 15)
pyplot.ylim(-15, 15)
# Mostrar la grafica.
pyplot.show()

print("Una vez vista la grafica, ingrese la ecuacion -0.5x^2+2.5x+4.5\n")
ecuacion = a, b, c = [float(input(f'Ingresa el coeficiente {coef}: ')) for coef in ('a', 'b', 'c')]
while a != 0.5 and b != 2.5 and c != 4.5:
    print("No ingreso los coeficientes indicados en la ecuacion -0.5x^2+2.5x+4.5 \n")
    ecuacion = a, b, c = [float(input(f'Ingresa el coeficiente {coef}: ')) for coef in ('a', 'b', 'c')]
primer_punto = float(input("ingrese el primer punto en la grafica: "))
segundo_punto = float(input("ingrese el segundo punto en la grafica: "))
iteracion = int(input("Ingrese las iteraciones deseadas: "))
while iteracion <= 0:
    print("Las iteraciones ingresadas deben ser mayores a 0\n")
    iteracion = int(input("Ingrese las iteraciones deseadas: "))
error = int(input("Ingrese el porcentaje de error deseado: "))
while error <= 0:
    print("El error deseado no puede ser negativo")
    error = int(input("Ingrese el porcentaje de error deseado: "))
print("\nRegula-Falsi:\n")

regula_falsi(lambda x: -a * (x ** 2) - b * x + c, primer_punto, segundo_punto, iteracion, error)
