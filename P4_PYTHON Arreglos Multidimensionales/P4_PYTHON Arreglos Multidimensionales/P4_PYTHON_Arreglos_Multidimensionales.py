maxf = 3
maxc = 5

# Crear una matriz vac�a
a = [[0.0] * maxc for _ in range(maxf)]

# Leer valores para llenar la matriz
for f in range(maxf):
    for c in range(maxc):
        a[f][c] = float(input(f'Ingrese el valor para a[{f}][{c}]: '))

# Imprimir la matriz
for f in range(maxf):
    for c in range(maxc):
        print(a[f][c], end=" ")
    print()  # Agregar una nueva l�nea despu�s�de�cada�fila
