from tkinter import *
import tkinter
# if 2 < 5:
#     print("EL numero 2 es menor")


#  a == b
#  a < b
#  a > b
#  a != b
# a <= b
# a >= b

# if 2 == 2:
#     print("2 es igual a 2")

# if 2 == 3:
#     print("2 es igual a 3")

# if 2 > 5:
#     print("2 es mayor a 5")
# if 5 > 2:
#     print("5 es mayor a 2")

# if 3 != 2:
#     print("3 es distinto a 2")

# if 2 >= 2:
#     print("3 es mayor o igual a 2")
if 2 > 5:
    print("2 es menor que 5 en if")
elif 2 > 5:
    print("2 es menor a 5 en elif")
elif 2 < 5:
    print("2 es menor a  en segundo elif")
else:
    print("yo me imprimo solo si todo lo anterior evalua en falso")


if 2 > 5:
    print("2 es menor que 5 en if")
else:
    print("Yo me impirmo solo si todo lo anterior evalua en falso 2")


# Operador ternario
if 2 < 5:
    print("if de una linea")
print("cuando devuelve true ") if 5 > 2 else print("cuando devuelve falso")


# And y OR
if 2 < 5 and 3 > 2:
    print("Ambas devueleve True")

if 2 > 5 and 3 > 2:
    print("Hay una falsa esto no se mostrara")

if 1 < 0 or 1 > 0:
    print("Una de las dos condiciones devolvio True")

if 1 < 0 or 1 < 0: 
    print("Si amabas condiciones evaluan en false no se ejecuta esto")

if 10 > 5 and 1 < 5:
    print("El numero se encuntra en el rango de 1 a 5") 

entrada = float(input("Digite un valor entre 1 y 10"))

entrada2 = float(input("Digite un valor entre 1 y 10"))
suma = entrada + entrada2
print(f"La suma de {entrada} + {entrada2} es igual a {suma} " )


root = Tk()
label = Label(root,text="Numero 1").pack( )
Label(root,text="Numero 1").pack()
Label(root,text="Numero 2").pack()
Entry(root,text="Numero 1",justify="left").pack() 
root.mainloop()








