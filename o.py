#author: Jay Sanders
#class: CS 325
#due: 2024-03-01

#this program uses an abstract shape class that every shape subclass can inherit from , so developers are able to add new shapes without modifying the square class, and can add new functionality to the square class without changing the existing functions

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
class Square(Shape):
    def __init__(self, base):
        self.base = base
    def get_area(self):
        return pow(self.base, 2)
def main():
    square = Square(4)
    print(square.get_area())
if __name__ == "__main__":
    main()