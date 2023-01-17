import os 
os.system('cls')

#Las tuplas son inmutables, no se puede modificar
tupla = (12,345,'Hola', 'Mundo', 'Somos', 'Una', 'Tupla')
print(tupla)
print(tupla.count('Mundo'))  # Contar cuantos datos existen de Mundo
print(tupla.index('Mundo'))  # Indice en donde se encuentra el valor

listaDeTupla = list(tupla)
print(listaDeTupla.append('Chanchito triste'))
print(listaDeTupla)


# Rango 

rango = range(6)
print(rango)
