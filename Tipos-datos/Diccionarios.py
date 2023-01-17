import os 
os.system('cls')

diccionarios = {
    "nombres": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

# print(diccionarios)
# # Accediendo con el metodo get a un dato del diccionario
# print(diccionarios.get('nombres'))
# print("\n")
# diccionarios['nombres'] = 'Flufly'
# print(diccionarios)
# print(len(diccionarios))

diccionarios['ronronea'] = 'SI'
print(diccionarios)
# diccionarios.pop('ronronea')
print(diccionarios)

# diccionarios.popitem()
# copiaGatito = diccionarios.copy()
copiaGatito = dict(diccionarios)
# del diccionarios['ronronea']
diccionarios.clear()
print(diccionarios,copiaGatito)










