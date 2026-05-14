#Ejercicio 1: Validador de edad para eventos

## Enunciado(10 ptos)

'''Crea un programa que permita registrar varias personas para un evento.
 Por cada persona se debe pedir su nombre y edad.

Reglas:

- Menor de 12 años: no puede ingresar.
- Entre 12 y 17 años: puede ingresar con acompañante.
- Mayor o igual a 18 años: puede ingresar solo.
- El programa debe repetirse hasta que el usuario escriba `"salir"` como nombre.'''

while True:
    nombre = input("Ingrese el nombre de la persona o 'salir' para terminar: ")

    if nombre.lower() == "salir":
        print("Registro finalizado.")
        break

    edad = int(input("Ingrese la edad: "))

    if edad < 12:
        print(nombre, "no puede ingresar al evento.")
    elif edad >= 12 and edad <= 17:
        print(nombre, "puede ingresar solo con acompañante.")
    else:
        print(nombre, "puede ingresar solo.")