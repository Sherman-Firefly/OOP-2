import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  
    
    def area(self):
        "Calculate the area."
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        "Calculate the circumference."
        return 2 * math.pi * self.radius


radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.area():.2f}")
print(f"Circumference of the circle: {circle.perimeter():.2f}")
