
from mimetypes import init


class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print("Hola, soy un", self.tipo,  "y mi sonido es el ", self.onomatopeya)


class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self,nombre, onomatopeya)
        print('Hola, soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Instanciando un perro")

class Canario(Animal):
    tipo = 'canario'


gato = Gato('Flugly', 'Maullido')
gato.saludo()
perro = Perro('Firulais', 'Ladrido')
perro.saludo()
canario = Canario('Piolin', 'silvido')
canario.saludo()

