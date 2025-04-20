#PRACTICO 4- EJERCICIO 4
#ENCONTRAR LA SUMA DE LOS NUMEROS INGRESADOS
#A numero SE LE DA UN VALOR DISTINTO DE CERO CUALQUIERA, EN ESTE CASO 400, PARA EMPEZAR EL while.
# EN EL PRIMER CICLO DE while SE CAMBIA EL VALOR DE numero = 400 POR EL 1ER NUMERO INGRESADO
numero = 400
acumulado = 0
while numero != 0:
    numero = int(input("Ingrese un numero entero: "))
    acumulado = acumulado + numero
print(f"La suma de los numeros ingresado es: {acumulado}")
print("Fin programa")
