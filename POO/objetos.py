import os 
os.system('cls')


class Usuario:
    def __init__(self,nombre,apellido): 
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola Mi nombre es: ", self.nombre, self.apellido)



# Herencia

class Admin(Usuario):
    def superSaludo(self):
        print("Hola me llamo ", self.nombre," y  soy administrador")

usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Chanchito', 'Feliz')

usuario.saludo()
usuario.nombre = 'Chanchito'
usuario.saludo()
# del usuario.nombre
# usuario.saludo()
# del usuario
# print(usuario)

Admin = Admin('Super','Administrador')
Admin.saludo()
Admin.superSaludo()





