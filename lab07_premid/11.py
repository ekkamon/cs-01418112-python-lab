num = int(input())

_sum = -1

while num > 0:
  value = num % 10

  if value % 2 == 0:
    if _sum == -1:
      _sum = 1

    _sum *= value

  num //= 10

print(_sum)