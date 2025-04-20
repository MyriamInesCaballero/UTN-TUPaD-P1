# PRACTICO 5-1 SALUDA AL MUNDO
# DEFINICION DE FUNCIONES 
def segundos_horas(segundo):    
    horas = segundo / 3600
    return horas


#PROGRAMA PRINCIPAL
print("SEGUNDOS A HORAS")
segundos_ingresados = int(input("Ingrese los segundos= "))
horas = segundos_horas(segundos_ingresados)
print(f"{segundos_ingresados} son equivalente {horas} horas")
print("Fin del programa")