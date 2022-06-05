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


regula_falsi(lambda x: -0.5 * (x ** 2) - 2.5 * x + 4.5, -1.5, 2, 3, 1)
