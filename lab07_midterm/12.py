n = 0
is_win = -1
target = 0

while True:
  a = int(input())
  b = int(input())

  if a <= 0 or b <= 0 or a > 6 or b > 6:
    print('ERROR')
    continue
  else:
    n += 1

  _sum = a + b

  if _sum == target:
    is_win = True
    pass
  elif target != 0 and _sum == 7:
    is_win = False

  if n == 1:
    if _sum == 7 or _sum == 11:
      is_win = True
      pass
    elif _sum == 2 or _sum == 3 or _sum == 12:
      is_win = False
      pass
    else:
      target = _sum
  
  if is_win != -1:
    print(f'{n} {_sum} {"W" if is_win == True else "L"}')
    break

    