print("============================================================")
print("|      Calculadora basica implementada con excepciones     |")
print("============================================================")
numero = input("Ingrese primer numero: ")
try:
    numero = int(numero)
except:
    numero = "Chanchito feliz"
if numero == "Chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

numero2 = input("Ingrese segundo numero: ")
try:
    numero2 = int(numero2)
except:
    numero2 = "Chanchito feliz"


if numero2 == "Chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

simbolo = input("Ingrese operacion: ")
if simbolo == '+':
    print("===========================")
    print('Suma: ', numero + numero2)
    print("===========================")
elif simbolo == '-':
    print("===========================")
    print("resta: ", numero - numero2)
    print("===========================")
elif simbolo == '*':
    print("====================================")
    print("Multiplicacion: ", numero * numero2)
    print("====================================")
elif simbolo == '/':
    print("===========================")
    print("resta: ", numero / numero2)
    print("===========================")
elif simbolo == '%':
    print("===========================")
    print("resta: ", numero % numero2)
    print("===========================")
else:
    print("====================================")
    print("El simbolo ingresado no es valido")
    print("====================================")


