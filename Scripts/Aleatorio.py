#Python contiene muchas librerias listas para usarse.
#A las librerias tienen el nombre de Modules (module)
#Para utilizar in modulo en un script primero se tiene que
#importar, usando la instruccion import
import random

#Se define una varibale tipo float, y se le asigna un valor
numero1 = float(10.5)

#En python, una funcion es un conjunto de instrucciones que procesan una tarea
#en especifico, como una unidad de ejecucion.
#Este conjunto se declaran con def. Todo el codigo identado de la definicion,
#forma parte de la funcion.
def mifuncion():
    #Se convierte a float el numero aleatorio generado por
    #random.radrange() (solo esta disponible si se importa
    #el modulo random)
    numero2=float(random.randrange(1,10))
    #Se utilizan meta sustitucion para darle un orden logico al mensaje
    mensaje = ("La suma de {} y {} es {}")
    print(mensaje.format(numero1,numero2,numero1 + numero2))

#Se ejecuta la funcion que definimos
mifuncion()