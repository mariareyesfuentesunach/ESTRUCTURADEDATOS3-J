#Maria Jose Reyes Fuentes 3-J LSC
#Practica 06 - Vectores

#Declara una lista de cadenas
Aves = ["Loro gris", "Paloma de diamanete", "Coctel"]
print("Los valores de la lista antes de insertar: ")

#Itera sobre la lista para imprimir los valores
for ave in Aves:
    print(ave, end = " ")
    
print("\n")

#Agrega tres valores al final de la lista utilizando el metodo append()
Aves.append("Mayna")
Aves.append("Periquitos")
Aves.append("Cacatua")
print("Los valores de la lista despues de insertar: ")

#Itera sobre la lista para imprimir los valores
for ave in Aves:
    print(ave,end = " ")

print("\n")
