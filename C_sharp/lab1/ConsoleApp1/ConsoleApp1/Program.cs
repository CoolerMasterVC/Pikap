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

            double t1 = -1;
            double t2 = -1;


            double x1 = -100000, x2 = -100000, x3 = -100000, x4 = -100000;
            if (D < 0)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Нет действительных корней");
            }
            else
            {


                if (D == 0)
                {
                    t1 = (-b) / (2 * a);
                    //Console.WriteLine("Корень данного уравнения: {0}", t1);
                    if (t1 >= 0)
                    {
                        x1 = Math.Sqrt(t1);
                        x2 = -Math.Sqrt(t1);

                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine("Корни: {0}, {1}",x1,x2);
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Нет действительных корней");
                    }
                    
                }
                else
                {
                    bool flag = false;
                    D = Math.Sqrt(D);
                    t1 = (-b + D) / (2 * a);
                    t2 = (-b - D) / (2 * a);
                    //Console.WriteLine("Корни данного квадратного уравнения: {0}; {1}",
                    //(-b + D) / (2 * a), (-b - D) / (2 * a));


                    if (t1 >= 0)
                    {
                        flag = true;
                        x1 = Math.Sqrt(t1);
                        x2 = -Math.Sqrt(t1);
                    }
                    if (t2 >= 0)
                    {
                        flag = true;
                        x3 = Math.Sqrt(t2);
                        x4 = -Math.Sqrt(t2);
                    }
                    if (flag)
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.Write("Корни: ");
                        if (x1 != -100000)
                        {
                            Console.Write("{0}, {1} ", x1, x2);
                        }
                        if (x3 != -100000)
                        {
                            Console.Write("{0}, {1} ", x3, x4);
                        }
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Нет действительных корней");
                    }
                }
            }



            //Console.WriteLine("{0},{1},{2},{3}",a, b, c,D);
            Console.ResetColor();
            return 0;
        }
    }
}