#PRACTICO 4- EJERCICIO 5
#ADIVINAR UN NUMERO ALEATORIO ENTRE 0 - 9, Y INDICAR EL NUMERO DE INTENTOS PARA LOGRARLO
import random
incognita = random.randint(0,9)
intentos = 0
acertado = "false"
print("ADIVINA EL NUMERO")
while acertado == "false":
    numero = int(input("Ingrese un numero entero entre 0 -9: "))
    intentos+=1
    if incognita == numero:
        print(f"GANASTE!! ACERTATE!! INTENTO: {intentos} ")
        acertado = "true"
    else:
        print("PERDISTE!! VUELVE A INTENTARLO")
print("Fin programa")
