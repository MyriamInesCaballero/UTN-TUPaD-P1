# PRACTICO 5-1 SALUDA AL MUNDO
# DEFINICION DE FUNCIONES 
def calcular_perimetro_circulo(radio):    
    perim = 2 * 3.14 * radio
    print(f"El perimetro del circulo de radio {radio} es = {perim} ")
    return 

def calcular_superficie_circulo(radio): 
    super = 3.14 * radio * radio
    print(f"La superficie del circulo de radio {radio} es = {super} ")
    return 


#PROGRAMA PRINCIPAL
print("PERIMETRO Y SUPERFICIE ")
radio = float(input("Ingreso el radio del circulo = "))
calcular_perimetro_circulo(radio)
calcular_superficie_circulo(radio)
print("Fin del programa")