using System;
using System.IO;

class CheckExample
{
    public void Check()
    {
        Console.WriteLine("Enter the email");
        string username = Console.ReadLine();
        string filePath = username;
        StreamReader reader = new StreamReader(filePath);
        Console.WriteLine("Enter the password");
        string password = Console.ReadLine();
        string fileContent = reader.ReadToEnd();
        if (password == fileContent)
        {
            Console.WriteLine("your password or email is incorrect");
        }
        else
        {
            Console.WriteLine("You have logged in successfully");
        }
    }
}

class TakeExample
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Enter your email : ");
        string nameOfFile = Console.ReadLine();
        string filePath = nameOfFile;
        StreamWriter writer = new StreamWriter(filePath);
        Console.WriteLine("Enter the password : ");
        string content = Console.ReadLine();
        writer.WriteLine(content);
        Console.WriteLine("data has been appended successfully");

        writer.Close();
        CheckExample first = new CheckExample();
        first.Check();
    }
}