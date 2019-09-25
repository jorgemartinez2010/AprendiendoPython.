numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)
#for ejecuta un bloque de codigo un numero determinado de veces
#cuando se pida que recorra un rango de valore. El segundo parametro
#de range no se incluye en la serie de valores. Aqui seria del 1 al 10
for i in range(1,11):
    #i es la variable que cambia en cada iteracion
    salida = "{} x {} = {}"
    print(salida.format(numero, i, i*numero))