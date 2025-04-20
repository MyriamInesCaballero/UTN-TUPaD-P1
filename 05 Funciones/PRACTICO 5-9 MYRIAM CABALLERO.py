# PRACTICO 5-9 MYRIAM CABALLERO
#PASAR °CELSIUS A ° FAHRENHEIT
# DEFINICION DE FUNCIONES 
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return(fahrenheit)
        

#PROGRAMA PRINCIPAL
print("CELSIUS A FAHRENHEIT")
celsius_ingresado = float(input("Ingrese los grados en Celsius: "))

# LLAMA A LA FUNCION
resultado = celsius_a_fahrenheit(celsius_ingresado)
# DA LOS RESULTADOS
print("Resultados:")
print(f"{celsius_ingresado}°C es equivalente a {resultado}°F")
print("Fin del programa")