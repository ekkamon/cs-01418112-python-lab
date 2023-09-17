n = int(input())

i = 0
last_num = -1

while i < n:
  i += 1

  if n % i == 0:
    target = n / i

    if last_num != -1:
      if target * last_num == n:
        print(int(target + last_num))
        break
      elif target ** 2 == n:
        print(int(target + target))
        break

    last_num = target

if i == 1:
  print(int(1 + n))