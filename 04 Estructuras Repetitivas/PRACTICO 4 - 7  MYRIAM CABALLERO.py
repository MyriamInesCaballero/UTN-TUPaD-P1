#PRACTICO 4- EJERCICIO 7
#ENCONTRAR LA SUMA DE LOS NUMEROS COMPRENDIDOS ENTRE 0 y el ENTERO INGRESADO
inferior = 0
superior = int(input("ingrese un numero entero positivo: "))
acumulador = 0
while inferior < superior:
    inferior += 1
    acumulador = acumulador + inferior
print(f"la suma de los numeros es: {acumulador}")
print("Fin programa")
