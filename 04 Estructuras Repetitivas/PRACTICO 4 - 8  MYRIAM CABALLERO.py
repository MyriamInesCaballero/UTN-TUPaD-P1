#PRACTICO 4- EJERCICIO 8
#CONTAR LOS NUMEROS ENTEROS INGRESADOS EN PAR - IMPAR, Y EM POSITIVO NEGATIVO
par = 0
impar = 0
positivo = 0
negativo = 0
cero = 0
for x in range(100):
    numero = int(input("Ingrese un numero entero: "))
    if numero == 0:
        cero = cero + 1 
    else:
        resto = numero % 2
        if resto == 0:
            par = par + 1
        else:
            impar = impar + 1
        if numero > 0:
            positivo = positivo + 1
        else:
            negativo = negativo + 1
print(f"la cantidad de ceros es: {cero}")
print(f"la cantidad de numeros pares es: {par}")
print(f"la cantidad de numeros impares es: {impar}")
print(f"la cantidad de numeros positivos es: {positivo}")
print(f"la cantidad de numeros negativos es: {negativo}")
print("Fin programa")
