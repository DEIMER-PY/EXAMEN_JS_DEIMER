# EXAMEN_JS_DEIMER
# Ejercicio 1: Validador de edad para eventos

## Enunciado(10 ptos)

Crea un programa que permita registrar varias personas para un evento.
 Por cada persona se debe pedir su nombre y edad.

Reglas:

- Menor de 12 años: no puede ingresar.
- Entre 12 y 17 años: puede ingresar con acompañante.
- Mayor o igual a 18 años: puede ingresar solo.
- El programa debe repetirse hasta que el usuario escriba `"salir"` como nombre.

# Ejercicio 2: Sistema de descuentos por tipo de cliente

## Enunciado(20 ptos)

Crea un programa que calcule el total a pagar en una tienda.

El usuario debe ingresar:

- Nombre del cliente
- Tipo de cliente: `normal`, `premium` o `vip`
- Valor de la compra

Reglas:

- Cliente `normal`: sin descuento.
- Cliente `premium`: 10% de descuento.
- Cliente `vip`: 20% de descuento.
- Si la compra supera $500.000, se aplica un 5% adicional.

# Ejercicio 3: Promedio de notas con clasificación

## Enunciado (15 ptos)

Crea un programa que permita ingresar las notas de varios estudiantes.

Por cada estudiante se debe ingresar:

- Nombre
- Tres notas

El programa debe calcular el promedio y mostrar:

- `Excelente` si el promedio es mayor o igual a 4.5
- `Bueno` si está entre 3.8 y 4.4
- `Aceptable` si está entre 3.0 y 3.7
- `Reprobado` si es menor que 3.0

El programa debe preguntar cuántos estudiantes se van a registrar.

# Ejercicio 4: Análisis de riesgo sísmico en ciudades de Colombia (55 ptos)

## Enunciado

Se requiere desarrollar un programa en **Python** que permita registrar información sobre sismos ocurridos durante un día en **5 ciudades de Colombia**.

Para cada ciudad, el programa debe solicitar el nombre de la ciudad y leer una muestra de **5 magnitudes de sismos**.

El programa debe calcular el **promedio de magnitud sísmica** de cada ciudad y luego ordenar las ciudades de mayor a menor promedio.

Después de ordenar las ciudades, se debe asignar el nivel de riesgo según la posición que ocupe cada ciudad.

El programa debe desarrollarse usando **funciones**, específicamente:

1. Una función para calcular el promedio de los 5 sismos de una ciudad.
2. Una función para obtener el nivel de riesgo según la posición de la ciudad después del ordenamiento.

------

## Reglas para asignar el riesgo

Una vez calculados los promedios, las ciudades deben ordenarse de mayor a menor promedio.

| Posición | Clasificación |
| -------- | ------------- |
| 1        | Riesgo alto   |
| 2        | Riesgo medio  |
| 3        | Riesgo medio  |
| 4        | Riesgo bajo   |
| 5        | Sin riesgo    |

------

## Funciones requeridas

### 1. Función para obtener el promedio

Debe crear una función llamada `leer_promedio`.

Esta función debe recibir como parámetro el nombre de la ciudad, leer las 5 magnitudes de sismos y retornar el promedio.

```
def leer_promedio(ciudad):
    # Leer 5 sismos
    # Calcular la suma
    # Retornar el promedio
```

------

### 2. Función para obtener el riesgo

Debe crear una función llamada `obtener_riesgo`.

Esta función debe recibir como parámetro la posición de la ciudad después de ordenar los promedios y retornar el riesgo correspondiente.

```
def obtener_riesgo(posicion):
    # Retornar el riesgo según la posición
```

Ejemplo:

```
obtener_riesgo(1)  # Riesgo alto
obtener_riesgo(2)  # Riesgo medio
obtener_riesgo(3)  # Riesgo medio
obtener_riesgo(4)  # Riesgo bajo
obtener_riesgo(5)  # Sin riesgo
```

------

## Restricciones del ejercicio

El programa debe cumplir con las siguientes condiciones:

- Debe usar funciones.
- Debe usar `while` para leer los sismos.
- Debe usar `match` para asignar el riesgo.
- No debe usar listas.
- No debe usar diccionarios.
- No debe usar tuplas.
- Debe ordenar las ciudades de mayor a menor promedio.
- Debe mostrar el nombre de la ciudad, su promedio y su clasificación de riesgo.

------

## Proceso del programa

El programa debe realizar los siguientes pasos:

1. Solicitar el nombre de la primera ciudad.
2. Llamar a la función `leer_promedio` para leer sus 5 sismos y calcular el promedio.
3. Repetir el proceso para las 5 ciudades.
4. Ordenar las ciudades de mayor a menor promedio.
5. Usar la función `obtener_riesgo` para asignar el riesgo según la posición.
6. Mostrar los resultados finales.

------

## Salida esperada

El programa debe mostrar un resultado similar al siguiente:

```
RESULTADO DEL ANÁLISIS SÍSMICO
--------------------------------
Ciudad: Bucaramanga
Promedio: 4.62
Clasificación: Riesgo alto
--------------------------------
Ciudad: Medellín
Promedio: 3.24
Clasificación: Riesgo medio
--------------------------------
Ciudad: Bogotá
Promedio: 2.26
Clasificación: Riesgo medio
--------------------------------
Ciudad: Cali
Promedio: 1.70
Clasificación: Riesgo bajo
--------------------------------
Ciudad: Cartagena
Promedio: 0.70
Clasificación: Sin riesgo
--------------------------------
```