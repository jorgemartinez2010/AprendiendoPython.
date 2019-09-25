#Se captura un numero y se almacena en la variable numero
#y es convertido a tipo int
numero=int(input("Dame un numero entero: "))
#Se almacenan los valores booleanos la evaluacion de
#residuales. Si el residuo es cero, entonces el
#numero es multiplo.
esMultiplo3 = ((numero%3)==0)
esMultiplo5 = ((numero%5)==0)
esMultiplo7 = ((numero%7)==0)
#Cuando se usa el and, se resuelve por verdadero si todas
#las condiciones son verdaderas. Cuando se usa or, se resuelve
#como verdadero si al menos hay una condicion verdadera. Los
#parentesis le dicen a Pyhton que las primeras condiciones
#son juntas, y la tercera es una condicion independiente.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Es correcto")
else:
    print("Incorrecto")