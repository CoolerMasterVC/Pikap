using System;
using System.Text;
using System.Collections.Generic;
namespace Squed
{
    class Program
    {
        static int Main(string[] args)
        {
            double a, b, c;
            double D = -1;
            if (args.Length == 3)
            {
                a = Convert.ToDouble(args[0]);
                b = Convert.ToDouble(args[1]);
                c = Convert.ToDouble(args[2]);
                D = b * b - 4 * a * c;
            }
            else
            {
                string a_check, b_check, c_check;
                while (true)
                {
                    Console.WriteLine("Введите коэффициент а: ");
                    a_check = Console.ReadLine();
                    if (double.TryParse(a_check, out a))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Неверный ввод ");
                    }
                }
                while (true)
                {
                    Console.WriteLine("Введите коэффициент b:");
                    b_check = Console.ReadLine();
                    
                    if (double.TryParse(b_check, out b))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Неверный ввод.");
                    }
                }
                while (true)
                {
                    Console.WriteLine("Введите коэффициент c:");
                    c_check = Console.ReadLine();
                    
                    if (double.TryParse(c_check, out c))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Неверный ввод.");
                    }
                }
            }

            D = b * b - 4 * a * c;
            // определение наличия, количества и самих корней квадратного уравнения
            if (D < 0)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Уравнение не имеет действительных корней");
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Уравнение имеет следующие действительные корни: ");


                if (D == 0)
                {
                    Console.WriteLine("Корень данного уравнения: {0}", (-b) / (2 * a));
                }
                else
                {
                    D = Math.Sqrt(D);
                    Console.WriteLine("Корни данного квадратного уравнения: {0}; {1}",
                        (-b + D) / (2 * a), (-b - D) / (2 * a));

                }
            }
            //Console.WriteLine("{0},{1},{2},{3}",a, b, c,D);
            Console.ResetColor();
            return 0;
        }
    }
}