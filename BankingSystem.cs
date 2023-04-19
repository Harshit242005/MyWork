// class creation for the c#
// bank account class creation and solving real life problem
using System;

public class Account
{
    public String name;
    public int balance;
    public int account_num;

    public Account(string n, int b, int a)
    {
        name = n;
        balance = b;
        account_num = a;
    }

    public int Show()
    {
        return this.balance;
    }

    public void withdrwal(int x)
    {
        if ( x > this.balance)
        {
            Console.WriteLine("insufficient balnce");
        }
        this.balance = this.balance - x;
        Console.WriteLine("Letf ammount : "+ this.balance);
    }

    public void deposite(int y)
    {
        this.balance = this.balance + y;
        Console.WriteLine("After depositing the value is : "+ this.balance);
    }

    public void transfer(Account destination, int amount)
    {
        if (amount > this.balance) 
        {
            Console.WriteLine("insufficient amount");
        }
        else
        {
            this.balance -= amount;
            destination.balance += amount;
            Console.WriteLine("new balance of the current account : "+ this.balance);
            Console.WriteLine("new balance of other account :"+ destination.balance);
        }
    }
}

class test
{
    public static void Main(string[] args)
    {
        Account a1 = new Account("harshit", 1000, 123);
        Account a2 = new Account("andy", 2000, 789);
        Console.WriteLine(a1.Show());
        Console.WriteLine(a2.Show());
        a1.withdrwal(100);
        a1.deposite(1000);
        a1.transfer(a2, 1000);
    }
}