#PRACTICO 4- EJERCICIO 2
#ENCONTRAR DE CUANTOS DIGITOS ESTA FORMADO EL NUMERO INGRESADO
numero = int (input("Ingrese un numero entero: "))
#EN INGRESADO CONSERVO EL NUMERO PARA IMPRIMIRLO MAS BONITO
ingresado = numero
numero = abs(numero)
contador = 0
if numero == 0:
    print("El numero ingresado es cero, tiene un digito")
else:   
#contador VA CONTANDO LOS DIGITOS  
    while numero != 0:
        numero = int(numero // 10)
        contador += 1
    print(f"El numero {ingresado} esta compuesto por {contador} digitos")
print("Fin programa")