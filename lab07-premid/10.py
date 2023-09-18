num = int(input())

_sum = 0

while num > 0:
  value = num % 10

  if value % 2 > 0:
    _sum += value

  num //= 10

print(-1 if _sum == 0 else _sum)