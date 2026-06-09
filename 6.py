import math

# Base class
class Shape:
    def area(self):
        """Method to calculate area (to be implemented by subclasses)."""
        raise NotImplementedError("Subclass must implement this method")

    def perimeter(self):
        """Method to calculate perimeter (to be implemented by subclasses)."""
        raise NotImplementedError("Subclass must implement this method")


# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Subclass for Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side


# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        """Initialize with three sides a, b, c."""
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        """Use Heron's formula to calculate the area."""
        s = self.perimeter() / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
# Example usage
circle = Circle(5)
print(f"Circle: Area = {circle.area():.2f}, Perimeter = {circle.perimeter():.2f}")

square = Square(4)
print(f"Square: Area = {square.area():.2f}, Perimeter = {square.perimeter():.2f}")

triangle = Triangle(3, 4, 5)
print(f"Triangle: Area = {triangle.area():.2f}, Perimeter = {triangle.perimeter():.2f}")



