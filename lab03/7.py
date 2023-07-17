import math

x = float(input('Enter x : '))

result = 0

if x < 0:
    result = math.sqrt((x**2) + 1)
elif x == 0:
    result = x
elif x > 0 and x <= 99:
    result = 3 * (x**2) - ((1 - x) ** 2)
else:
    result = (2 * (x ** 3)) - (x / math.sqrt(x + 1))
    
    
print('f({:.2f}) = {:d}'.format(x, math.ceil(result)))