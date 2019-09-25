numero1 = input("Numero 1:")
numero2 = input("Numero 2:")
salida = "Numeros proporcionados: {} y {}. {}."
if(numero1==numero2):
    #Si los numeros son iguales ejecuta este codigo
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    #Condicionales anidadaas, if dentro de otro if
    #Si los numeros no son iguales ejecuta este bloque de if
    if numero1>numero2:
        #Nos dice si el primer numero es mayor al segundo
        print(salida.format(numero1, numero2, "El mayor es el primero"))
    else:
        # O de lo contrario, si el segundo es mayor al primero
        print(salida.format(numero1, numero2, "El mayor es el segundo"))