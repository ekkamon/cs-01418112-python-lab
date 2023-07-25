num = int(input())

if num <= 0:
  print('ERROR')
else:
  while True:
    if num <= 0:
      break

    print(num % 10)

    num = num // 10

