entrada = input()
print(type(entrada))
#La variable booleana contiene el resultado de verificar si
#lo que se capturo es un digito, y si no se encuentra un punto
#en lo capturado, lo que indicaria se que trata de un numero
#con decimales, es decir, tipo float. Si find retorna -1 quiere
#decir que lo buscado, en este caso un punto decimal no se encontro
#si esEntero es True(verdadero), lo capturado es entero.
esEntero =(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #Se ejecuta si la condicion es verdadera (True)
    print("Dato entero. ¡Muy Bien!")
else:
    #Se ejecuta si la condicion es falsa (False)
    print("Dato no es entero. Intentar nuevamente.")