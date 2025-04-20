#PRACTICO 4- EJERCICIO 10
#ENCONTRAR UN NUMERO CON LOS DIGITOS INVERTIDOS CON RESPECTO AL NUMERO INGRESADO 
numero = int(input("Ingresa un numero entero: "))
auxiliar = numero
invertido = 0
numero = abs(numero)
while numero != 0:
    resto = numero % 10
    numero = numero // 10
    invertido = resto + invertido * 10
if auxiliar < 0:
    invertido = -1 * invertido
print(f"{invertido} es el numero formado por los digitos invertido del numero {auxiliar}")
print("Fin programa")
