using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab2
{
    internal abstract class GeometricShape
    {
        protected string _name;
        protected float _area;
        public virtual void GetArea()
        {

        }
        public void SetName(string name)
        {
            _name = name;
        }
        
    }
}
