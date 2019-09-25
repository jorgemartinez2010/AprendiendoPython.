#Se decalra una vriable de tipo String, con una cadena de numeros
Numero="1234"

#Se muestra en pantalla el tipo de variable.
#La salida Type no es un string, nos muestra que tipo de dato es la variable.
print(type(Numero))

# Se hace la conversion de la cadena a un tipo de dato int.
Numero=int(Numero)

#Muestra en la pantalla el nuevo tipo de dato conservando la misma variable.
print(type(Numero))

#Se declara una varibale tipo string con meta sustitucion (en que posicion
# estara el valor que le daremos con format.)
salida="El numero utilizado es {}"

#Se muestra en pantalla el resultado. La meta sustitucion hace que la 
# variable que le dimos se coloque en la posicion de {}.
print(salida.format(Numero))