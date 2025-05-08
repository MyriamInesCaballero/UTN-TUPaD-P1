#PRACTICO 5 LISTA - EJERCICIO 8
# Lista inicial
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
indice = compras[1].index("fideos")
#Con indice automaticamente busco el lugar donde esta fideo en la lista del segundo cliente
#Como es el segundo elemento en esa sublista le corresponderia 1
compras[1][indice] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)