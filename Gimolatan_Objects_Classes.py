import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
radius_value = 5  # Set the radius value as needed
my_circle = Circle(radius_value)

# Calculate and print area
print(f"Area: {my_circle.area():.2f}")

# Calculate and print perimeter
print(f"Perimeter: {my_circle.perimeter():.2f}")
