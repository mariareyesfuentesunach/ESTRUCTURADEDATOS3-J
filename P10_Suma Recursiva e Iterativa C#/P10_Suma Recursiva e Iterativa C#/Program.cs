// Maria Jose Reyes Fuentes 3-J LSC
// Practica 10 - Suma Recursiva e Iterativa

using System;

class Program
{
    static int SumaIterativa(int n)
    {
        int suma = 0;
        while (n > 9)
        {
            suma += n % 10;
            n /= 10;
        }
        suma += n;
        return suma;
    }

    static int SumaRecursiva(int n)
    {
        if (n <= 9)
            return n;
        else
            return SumaRecursiva(n / 10) + n % 10;
    }

    static void Main()
    {
        int OPCION, Numero;

        Console.Write("Ingrese el número: ");
        Numero = int.Parse(Console.ReadLine());

        Console.Write("Escoja una opción (1 para suma Iterativa, 2 para suma Recursiva): ");
        OPCION = int.Parse(Console.ReadLine());

        if (OPCION == 1)
        {
            Console.WriteLine("Resultado: " + SumaIterativa(Numero));
        }
        else if (OPCION == 2)
        {
            Console.WriteLine("Resultado: " + SumaRecursiva(Numero));
        }
        else
        {
            Console.WriteLine("NO VALIDO");
        }
    }
}