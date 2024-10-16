using Lab2;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Lab2
{
    internal class Circle: GeometricShape, IPrint
    {
        private float _radius;

        public float Radius
        {
            get { return _radius; }
            set { _radius = value; }
        }
        public Circle(float radius)
        {
            Radius = radius;
            _name = "Круг";
            GetArea();
        }
        public override void GetArea()
        {
            _area = (float)Math.PI * _radius * _radius;
        }

        public override string ToString()
        {
            return _name + ":\n Радиус: " + _radius + "\n Площадь: " + _area;
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
}
