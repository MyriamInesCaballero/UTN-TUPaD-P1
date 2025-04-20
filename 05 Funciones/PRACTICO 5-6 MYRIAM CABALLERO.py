# PRACTICO 5-1 SALUDA AL MUNDO
# DEFINICION DE FUNCIONES 
def tabla_multiplicar(numero):    
    for x in range(0, 11):
        multiplicacion = numero * x
        print(f"{numero} x {x} = {multiplicacion}")
    return 


#PROGRAMA PRINCIPAL
print("TABLA DE MULTIPLICAR ")
numero_ingresado = int(input("Ingrese un numero entero positivo: "))
tabla_multiplicar(numero_ingresado)
print("Fin del programa")