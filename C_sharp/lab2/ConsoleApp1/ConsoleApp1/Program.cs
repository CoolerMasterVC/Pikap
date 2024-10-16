using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            float width = float.Parse(Console.ReadLine());
            float height = float.Parse(Console.ReadLine());
            Rectangle rectangle = new Rectangle(width, height);
            rectangle.Print();

            float length = float.Parse(Console.ReadLine());
            Square square = new Square(length);
            square.Print();

            float radius = float.Parse(Console.ReadLine());
            Circle circle = new Circle(radius);
            circle.Print();
        }
    }
}