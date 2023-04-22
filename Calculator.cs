// creating a calculator using the c#

using System;
public class Addition
{
    public int Add(int x, int y)
    {
        return x + y;
    }
}

public class Subtract
{
    public int Sub(int x, int y)
    {
        return x - y;
    }
}

public class Multiply
{
    public int Mult(int x, int y)
    {
        return x * y;
    }
}

public class Division
{
    public int Div(int x, int y)
    {
        return x / y;
    }
}

public class Calculator
{
    public static void Main(string[] args)
    {
        int x;
        Console.WriteLine("Enter first number : ");
        string first = Console.ReadLine();
        int.TryParse(first, out x);

        int y;
        Console.WriteLine("Enter second number : ");
        string second = Console.ReadLine();
        int.TryParse(second, out y);

        string operat;
        Console.WriteLine("Enter a operator : ");
        operat = Console.ReadLine();

        if (operat == "+")
        {
            Addition a = new Addition();
            Console.WriteLine(a.Add(x, y));
        }

        if (operat == "-")
        {
            Subtract a = new Subtract();
            Console.WriteLine(a.Sub(x, y));
        }

        if (operat == "*")
        {
            Multiply a = new Multiply();
            Console.WriteLine(a.Mult(x, y));
        }

        if (operat == "/")
        {
            Division a = new Division();
            Console.WriteLine(a.Div(x, y));
        }
    }
}