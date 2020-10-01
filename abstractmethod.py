from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0;
class Rectangle(Shape):
    def __init__(self):
        self.length=3
        self.breadth=5
    def printarea(self):
        return 0;
rec1=Rectangle()
