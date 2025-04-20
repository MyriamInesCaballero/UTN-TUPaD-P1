# PRACTICO 5-10 MYRIAM CABALLERO
#PROMEDIO DE 3 NUMEROS

# DEFINICION DE FUNCIONES 
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return(promedio)
        

#PROGRAMA PRINCIPAL
print("CALCULO DE PROMEDIO")
num1 = float(input("Ingresa el 1° numero: "))
num2 = float(input("Ingresa el 2° numero: "))
num3 = float(input("Ingresa el 3° numero: "))

# LLAMA A LA FUNCION
resultado = calcular_promedio(num1, num2, num3)
# DA LOS RESULTADOS
print("Promedio:")
print(f"el promedio de los numeros ingresados es: {resultado}")
print("Fin del programa")