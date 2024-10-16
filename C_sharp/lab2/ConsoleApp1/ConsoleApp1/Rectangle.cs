using Lab2;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Lab2
{
    internal class Rectangle: GeometricShape, IPrint
    {
        protected float _width;
        protected float _height;

        public float Width
        {
            get { return _width; }
            set { _width = value; }
        }
        public float Height
        {
            get => _height;
            set => _height = value;
        }
        public Rectangle(float length)
        {
            Width = length;
            Height = length;
            _name = "Прямоугольник";
            GetArea();
        }
        public Rectangle(float width, float height)
        {
            Width= width;
            Height = height;
            _name = "Прямоугольник";
            GetArea();
        }
        public override void GetArea()
        {
            _area = _width * _height;
        }

        public override string ToString()
        {
            return _name + ":\n Ширина: " + _width + "\n Высота: " + _height + "\n Площадь: " + _area;
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
}
