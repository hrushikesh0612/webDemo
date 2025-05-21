import math

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius):
    return math.pi * radius * radius

# Example usage:
print("Python Program:")
print("Area of triangle with base 5 and height 10:", area_of_triangle(5, 10))
print("Area of rectangle with length 4 and width 6:", area_of_rectangle(4, 6))
print("Area of circle with radius 3:", area_of_circle(3))
