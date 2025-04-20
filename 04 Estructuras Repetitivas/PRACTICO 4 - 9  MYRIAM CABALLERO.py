#PRACTICO 4- EJERCICIO 9
#ENCONTRAR LA MEDIA DE LOS 100 NUMEROS ENTEROS INGRESADOS 
acumular = 0.0
for x in range(100):
    numero = int(input("Ingresa un numero entero: "))
    numero = float(numero)    
    acumular = float(acumular + numero)    
media = float(acumular / 100)
print(f"la media de los valores ingresado es: {media}")
print("Fin programa")
