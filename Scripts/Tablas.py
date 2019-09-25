for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #Un print sin argumentos es un salto de linea
    print()
    #Dentro de un for, se pone otro for.
    for j in range(1,11):
        #Aqui, i contiene el numero base de la tabla (i = es el numero de la tabla).
        #y j el elemento de la tabla(por cual numero se va a multiplicar).
        salida = "{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al termininar con las iteracioes que indicamos
        #se ejecuta este codigo, que es un salto de linea
        #y conclusion del for
        print()