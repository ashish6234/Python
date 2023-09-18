from abc import ABC, abstractmethod

# Define an abstract base class "Shape"
class Shape(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_name(self):
        return self.__name

# Define a subclass "Circle" that inherits from "Shape"
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.__radius

# Define a subclass "Rectangle" that inherits from "Shape"
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

# Create instances of Circle and Rectangle
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)

# Calculate and display area and perimeter for each shape
print(f"{circle.get_name()}: Area={circle.area()}, Perimeter={circle.perimeter()}")
print(f"{rectangle.get_name()}: Area={rectangle.area()}, Perimeter={rectangle.perimeter()}")
