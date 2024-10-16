using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Lab2
{
    internal class Square : Rectangle, IPrint
    {
        public Square(float length) : base(length)
        {
            _name = "Квадрат";
            GetArea();
        }

        public override string ToString()
        {
            return _name + ":\n Сторона: " + _width + "\n Площадь: " + _area;
        }
    }
}
