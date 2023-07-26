a = int(input())
b = int(input())
c = int(input())

if a > b:
  _b = b
  b = a
  a = _b

if a > c:
  _c = c
  c = a
  a = _c

if b > c:
  _c = c
  c = b
  b = _c

print('True' if (a ** 2) + (b ** 2) == (c ** 2) else 'False')