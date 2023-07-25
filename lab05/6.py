num = int(input())

_sum = 0

while True:
  if num <= 0:
    break

  _sum += num % 10

  num = num // 10

if _sum % 9 == 0:
  print(f'Yes {_sum}')
else:
  print(f'No {_sum % 9}')