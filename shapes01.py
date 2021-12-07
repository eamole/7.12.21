#shapes

import math

class Shape:

    shapes = []
    
    def __init__(self, name):
        self.name = name
        Shape.shapes.append(self)
        
    def __str__(self):
        return f"Shape: {self.name}"
    
    # define the interface of 
    def perimeter(self):
        print(f"This method <perimeter> should be overridden in the derived class {self}")
        return 0
    
    def area(self):
        print(f"This method <area) should be overridden in the derived class {self.name}")
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def area(self):
        return self.width * self.height

class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, width)
        self.name = "Square"
        

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius =  radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(2, 4)
print("Rect : ", rect.perimeter(), rect.area())

square = Square(4)
print("Square : ", square.perimeter(), square.area())


tri = Triangle(4, 5)
print("Rect : ", tri.perimeter(), tri.area())

circ = Circle(5)
print("Circle : ", circ.perimeter(), circ.area())

    
