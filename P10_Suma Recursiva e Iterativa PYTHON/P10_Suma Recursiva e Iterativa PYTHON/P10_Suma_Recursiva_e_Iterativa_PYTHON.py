# Maria Jose Reyes Fuentes 3-J LSC
# Practica 10 - Suma Recursiva e Iterativa Python

def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    suma += n
    return suma

def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

def main():
    OPCION = int(input("Ingrese el numero: "))
    Numero = int(input("Escoja una opcion (1 para suma Iterativa, 2 para suma Recursiva): "))

    if Numero == 1:
        print("Resultado:", suma_iterativa(OPCION))
    elif Numero == 2:
        print("Resultado:", suma_recursiva(OPCION))
    else:
        print("No valido")

if __name__ == "__main__":
    main()
