import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width


calculator = GeometryCalculator()

radius = 5
print(calculator.calculate_circle_area(radius))

calculator = GeometryCalculator()

length = 10
width = 6
print(calculator.calculate_rectangle_area(length, width))

calculator = GeometryCalculator()

length = 10
width = 6
print(calculator.calculate_rectangle_area(length, width))

