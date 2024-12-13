from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5 * self.base * self.height
rect=Rectangle(20, 5)
print(f"Rectangle area: {rect.area()}")
tri=Triangle(3, 4)
print(f"Triangle area: {tri.area()}")
