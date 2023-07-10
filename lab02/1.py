import math

radius = int(input("Enter a radius: "))

print("Area of a circle with radius {:d} is {:.2f}".format(radius, math.pi * (radius ** 2)))
print("Circumference of a circle with radius {:d} is {:.2f}".format(radius, 2 * math.pi * radius))