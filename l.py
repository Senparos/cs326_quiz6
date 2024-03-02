#author: Jay Sanders
#class: CS 325
#due: 2024-03-01

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
class HasWidthHeight(ABC):
    @abstractmethod
    def set_width(self, width):
        pass
    @abstractmethod
    def set_height(self, height):
        pass
class Circle(Shape, HasWidthHeight):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
class Rectangle(Shape, HasWidthHeight):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def set_base(self, base):
        self.base = base
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return 0.5 * self.base * self.height
    
def main():
    circle = Circle(5, 5)
    rectangle = Rectangle(4, 5)
    triangle = Triangle(2, 4)
    print(f"The area of the Circle is {circle.get_area()}")
    print(f"The area of the Rectangle is {rectangle.get_area()}")
    print(f"The area of the Triangle is {triangle.get_area()}")

if __name__ == "__main__":
    main()