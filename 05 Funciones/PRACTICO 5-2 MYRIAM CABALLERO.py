# PRACTICO 5-1 SALUDA AL MUNDO
# DEFINICION FUNCION
def saludar_usuario(nombre):
    saludo = "Hola " + nombre +"!"
    return saludo

#PROGRAMA PRINCIPAL
nombre_ingresado = input("¿Cual es tu nombre?: ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)
