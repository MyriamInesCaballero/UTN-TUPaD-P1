# PRACTICO 5-1 SALUDA AL MUNDO
# DEFINICION FUNCION
def informacion_personal(nombre, apellido, edad, residencia):    
    print("Soy", nombre, apellido, "tengo", edad, "años y vivo en", residencia + "." )
    return 

def validar_edad():
    while True: 
        edad = input ("Ingrese la Edad: ")
        if edad.isdigit():
            numero = int(edad)
            if numero > 0:
                return numero
            else:
                print("la edad debe ser mayor que cero")
        print("Ingrese solo numeros enteros positivos")


#PROGRAMA PRINCIPAL
print("Ingreso de datos personales")
nombre_ingresado = input("Ingrese su nombre: ")
apellido_ingresado = input("Ingrese su apellido: ")
edad_ingresado = validar_edad()
residencia_ingresado = input("Ingrese su residencia: ")
informacion_personal(nombre_ingresado,apellido_ingresado, edad_ingresado, residencia_ingresado)
