print("Programa que verifica si un dato de la lista existe")
dato = input("Ingrese el dato que desea buscar ")

lista = ['hola', 'mundo','chanchito', 'feliz', 'dragones']


if lista.count(dato) > 0:
    print(f'La palabra {dato} si existe  y se encuentra en la posicion {lista.index(dato)}')
else:
    print(f'La palabra {dato} no existe :(')

