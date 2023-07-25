import math

_sum = 0
count = 0
_min = math.inf
_max = -math.inf

while True:
  num = str(input())

  if num == '':
    break

  num = float(num)

  if num < _min:
    _min = num

  if num > _max:
    _max = num

  _sum += num
  count += 1

avg = _sum / count

print(f'{_max:.2f}', f'{_min:.2f}')
print(f'{_sum:.2f}', f'{avg:.2f}')