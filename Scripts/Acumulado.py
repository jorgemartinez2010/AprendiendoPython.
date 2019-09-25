#Se declaran las variables que usaremos con su tipo de dato.
acumulado = int(0)
numero = str("")

#Al poner True como condicion en While, se forma un
#ciclo infinito que no finalizara hasta que de forma
#explicita se utulice la instruccion break
while True:
    numero = input("Dame un numero entero: ")
    if numero== "":
        #Si el numero es vacio, se muestra en pantalla y sale.
        print("Vacio, salida del programa.")
        break
    else:
        #Se si registro un valor, acumulado = acumulado + numero
        #Se realiza el calculo usando la suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))