#PRACTICO 5 LISTA - EJERCICIO 6
#Creo la lista que se forma salteando 5, en el rango 10,30. Aclaro pongo 31 para que incluya el 30
numeros = list(range(10, 31, 5))

#Imprimo cada elemento de la lista
print("El primer elemento de la lista es: ", numeros[0])  # Primer número
print("El segundo elemento de la lista es: ", numeros[1])  # Segundo número

#Imprimo ahora una sublista con estos 2 elementos
print("O como sublista")
print(numeros[:2])  # Muestra los dos primeros como una sublista

print("Fin del Programa")