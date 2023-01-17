from turtle import RawTurtle


def MiFuncion():
    print("Mi primera Funcion")


# MiFuncion()

def imprimeDato(*nombre):
    print("El nombre completo es: ", nombre[1])

# imprimeDato('Chanchito', 'feliz','lala','lele','lili','lolo')


def nombreCompleto(apellido,nombre):
    print(nombre,apellido)

# nombreCompleto(nombre='Mateo',apellido='Rodriguez')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

# nombreCompleto(nombre='Chanchito', apellido='Feliz')


def miFuncion2(argumento='Chanchito'):
    print(argumento)


# miFuncion2('Batman')
# miFuncion2('')

def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['Chanchito', 'Feliz'])


def ConcatenaNombres(lista):
    i = ''
    for el in lista:
        i = i +  el + ' '
    return i

nombres = ConcatenaNombres(['Chanchito', 'Feliz'])
print(nombres)
 





