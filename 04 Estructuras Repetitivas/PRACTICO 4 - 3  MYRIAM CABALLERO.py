#PRACTICO 4- EJERCICIO 3
#ENCONTRAR LA SUMA DE LOS NUMEROS COMPRENDIDOS ENTRE 2 ENTEROS
print("Ingrese un intervalo (a,b)")
inferior = int (input("Ingrese el primer numero del intervalo, debe ser entero: "))
superior = int (input("Ingrese el segundo numero del intervalo, debe ser entero: "))
acumulador = 0
while inferior < superior - 1:
    inferior += 1
    acumulador = acumulador + inferior   
print(f"la suma de los numeros {acumulador}")
print("Fin programa")
