# PRACTICO 5-7 SALUDA AL MUNDO
#OPERACIONES BASICAS
# DEFINICION DE FUNCIONES 
def operaciones_basicas(a, b):    
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return(suma, resta, multiplicacion, division)
        

#PROGRAMA PRINCIPAL
print("OPERACIONES BASICAS")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
# LLAMA A LA FUNCION
resultados = operaciones_basicas(num1, num2)
# DA LOS RESULADOS
print("\nResultados:")
print("Suma: ", resultados[0])
print("Resta: ", resultados[1])
print("Multiplicacion: ", resultados[2])
print("Division: ", resultados[3])
print("Fin del programa")