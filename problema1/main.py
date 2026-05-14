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