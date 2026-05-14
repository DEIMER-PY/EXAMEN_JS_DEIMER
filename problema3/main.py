cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))

for i in range(cantidad):
    print("\nEstudiante", i + 1)

    nombre = input("Ingrese el nombre: ")

    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 4.5:
        clasificacion = "Excelente"
    elif promedio >= 3.8:
        clasificacion = "Bueno"
    elif promedio >= 3.0:
        clasificacion = "Aceptable"
    else:
        clasificacion = "Reprobado"

    print("Nombre:", nombre)
    print("Promedio:", round(promedio, 2))
    print("Clasificación:", clasificacion)