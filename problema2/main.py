#Ejercicio 2: Sistema de descuentos por tipo de cliente

## Enunciado(20 ptos)

'''
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
'''

nombre = input("Ingrese el nombre del cliente: ")
tipo_cliente = input("Ingrese el tipo de cliente normal/premium/vip: ").lower()
valor_compra = float(input("Ingrese el valor de la compra: "))

descuento = 0

match tipo_cliente:
    case "normal":
        descuento = 0
    case "premium":
        descuento = 0.10
    case "vip":
        descuento = 0.20
    case _:
        print("Tipo de cliente no válido")
        descuento = 0

if valor_compra > 500000:
    descuento += 0.05

valor_descuento = valor_compra * descuento
total_pagar = valor_compra - valor_descuento

print("Cliente:", nombre)
print("Valor compra:", valor_compra)
print("Descuento aplicado:", valor_descuento)
print("Total a pagar:", total_pagar)



