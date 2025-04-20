# PRACTICO 5-8 IMC
#CALCULO DEL INDICE DE MASA CORPORAL
# DEFINICION DE FUNCIONES 
def calcular_imc(peso, altura):    
    imc = peso / (altura * altura)
    return(imc)
        

#PROGRAMA PRINCIPAL
print("CALCULO DEL INDICE DE MASA CORPORAL")
peso = float(input("Ingrese el PESO en kg: "))
estatura = float(input("Ingrese la ESTATURA en m: "))
# LLAMA A LA FUNCION
imc_calculado = calcular_imc(peso, estatura)
# DA LOS RESULTADOS
print("Resultados:")
print(f"El indice de masa corporal es: {imc_calculado:.2f} ")
print("Fin del programa")