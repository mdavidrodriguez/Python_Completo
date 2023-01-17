#  =========================================================================
# # Multiplicar dos numeros sin usar el simbolo de la multiplicación
#  =========================================================================
from unittest import result
import math
a = 4
b = 8

resultado = 0
for x in range(a):
    resultado += b
print(resultado)
# Ingresar nombre y apellido e imprimirlos alreves

nombre = 'Mateo'
apellido = 'Rodriguez'

concatenacion = nombre + ' ' + apellido
print(concatenacion[::-1])


#  =========================================================================
# Escribir una funcion que encuentre el elemento menor de la lista
#  =========================================================================

lista = [1, 2, 5, 3, 55, -23, 4, -13]
menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor
print("Menor: ", menor)

#  =========================================================================
# Escribir una Funcion que devuelva el volumen de una esfera por su radio
#  =========================================================================
# 4 / 3 * pi * r ** 3


def calcularVolumen(r):
    return 4 / 3 * math.pi * r ** 3


resultado = calcularVolumen(6)
print(resultado)

#  =========================================================================
# Escribir una funcion que indique si el usuario es mayor de edad
#  =========================================================================


def esMayor(usuario):
    return usuario.edad > 17


class Usuario:
    def __init__(self, edad):
        self.edad = edad


usuario = Usuario(15)
usuario2 = Usuario(21)
resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)
print(resultado1, resultado2)

#  =========================================================================
# Escribir una funcion que indique si un numero es par o impar
#  =========================================================================


def esPar(n):
    return n % 2 == 0


resultado = esPar(11)
print(resultado)

#  =========================================================================
# Escribir una funcion que indique cuantas vocales tiene una palabra
#  =========================================================================

palabra = 'chAnchito feliz'
vocales =
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
print(vocales)


#  =========================================================================
# Escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir
# basta, luego que devuelva la suma de los numeros ingresados
#  =========================================================================

lista = []
print("Ingrese Numeros y para salir escriba basta")
while True:
    valor = input('Ingrese un valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato valido')
            exit()
resultado = 0

for x in lista:
    resultado += x
print(resultado)


#  =========================================================================
# Escribir una funcionq que escriba nombre y apellido y los vaya agregando a un  archivo
#  ========================================================================= 

def agregaNombreArchivo(nomnbre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nomnbre + ' ' + apellido + '\n')
    c.close()


agregaNombreArchivo('Chanchito', 'Bueno')

lista = [1,2,4,6,74,'Mateo Rodriguez']
valores = input("ingrese una cadena: ")
lista.append(valores)
print("Valores de la lista")
for i in lista:
    print(i)
