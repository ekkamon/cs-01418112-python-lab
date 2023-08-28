import math

radius = float(input('Enter a radius: '))

def circle(r):
    return math.pi * (r**2)

def circumference(r):
    return 2 * math.pi * r

def sphere(r):
    return (4/3) * math.pi * (r**3)

r = radius

print('Area of a circle with radius %.2f is %.2f.' % (r, circle(r)))
print('Circumference of a circle with radius %.2f is %.2f.' % (r, circumference(r)))
print('Volume of sphere with radius %.2f is %.2f.' % (r, sphere(r)))
    