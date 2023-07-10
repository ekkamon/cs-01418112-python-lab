import math

x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

print('a1 = {:.2f}'.format((x**y) + z))
print('a2 = {:.2f}'.format(math.cos(2 * math.pi) + math.log(x, math.e)))
print('a3 = {:.2f}'.format(abs(x) + abs(y)))
print('a4 = {:.2f}'.format(math.sqrt(x ** 2 + y ** 2 + z ** 2)))
print('a5 = {:.2f}'.format(math.sin(x) ** 2 + math.cos(x) ** 2))
print('a6 = {:.2f}'.format((x + y) ** (1/5)))
print('a7 = {:.2f}'.format(math.e ** (x * math.log(y, math.e))))
