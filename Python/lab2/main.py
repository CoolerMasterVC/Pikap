from python_oop.shape import Rectangle, Circle, Square
import numpy as np

if __name__ == "__main__":
    N = 5

    rectangle = Rectangle(N, N, "blue")
    circle = Circle(N, "green")
    square = Square(N, "red")

    print(rectangle)
    print(circle)
    print(square)

    
    print("Сумма чисел от 1 до N:", np.sum(range(1, N + 1)))