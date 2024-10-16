from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Color:
    def __init__(self, color_name):
        self.color_name = color_name

class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Rectangle(width={}, height={}, color={}, area={})".format(
            self.width, self.height, self.color.color_name, self.area()
        )
    
class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "Circle(radius={}, color={}, area={:.2f})".format(
            self.radius, self.color.color_name, self.area()
        )

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "Square(side={}, color={}, area={})".format(
            self.width, self.color.color_name, self.area()
        )