#Ejercicio 3: Promedio de notas con clasificación

## Enunciado (15 ptos)

'''Crea un programa que permita ingresar las notas de varios estudiantes.

Por cada estudiante se debe ingresar:

- Nombre
- Tres notas

El programa debe calcular el promedio y mostrar:

- `Excelente` si el promedio es mayor o igual a 4.5
- `Bueno` si está entre 3.8 y 4.4
- `Aceptable` si está entre 3.0 y 3.7
- `Reprobado` si es menor que 3.0

El programa debe preguntar cuántos estudiantes se van a registrar.'''

# 

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