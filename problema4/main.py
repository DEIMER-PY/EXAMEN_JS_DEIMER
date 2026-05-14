# Ejercicio 4: Análisis de riesgo sísmico en ciudades de Colombia (55 ptos)
## 

def nivel_sismo(Magnitud):
    if Magnitud < 3:
        return "leve"
    elif Magnitud < 5:
        return "moderado"
    elif Magnitud < 7:
        return "alto riesgo"
    else:
        return "Grave"
    
ciudad = ""
while ciudad != "salir":
    ciudad = input("Ingrese la ciudad (o escriba salir para finalizar el programa): ").lower()
    if ciudad != "salir":
        magnitud = float(input("Ingrese magnitud del sismo: "))
        print("-" * 20)
        print("RESULTADO DEL ANÁLISIS SÍSMICO")
        print("-" * 20)
        print("ciudad:",ciudad)
        print("-" * 20)
        print("nivel de sismo es:", nivel_sismo(magnitud))
        print("-" * 20)

    