import os 
os.system('cls')

lista = [1,2,3,3,3,3]  # Lista vacia


# Agregando datos a la lista
print("Sacamos datos de la lista")
lista.append(4)  
lista.append(5)
lista.append(6)
print(lista)

print("\nYa eliminamos los datos de la lista")
lista.pop()
lista.pop()
lista.pop()
print(lista)  # Sacando datos de la lista

print("\nvaciamos la lista con clear")
# lista.clear()
# print(lista)

print("\ncopiamos los datos de la lista con copy")
lista2 = lista.copy()
print(lista, lista2)


print("\nContando elemento de la lista con count")
# Contando elementos de la lista 
print(lista.count(3))


# Contando la cantidad de elementos de la lista
print("Elementos de la lista 1 ")
print(len(lista))



# Largo de las dos listas
largoLista = len(lista)
largoLista2 = len(lista2)

print(largoLista,largoLista2)




