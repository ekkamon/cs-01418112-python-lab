num = int(input('Enter a number: '))
digit = int(input('Enter a digit: '))

is_error = False
times = 0

if num < 0:
  is_error = True
  print('Invalid number.')

if digit < 0 or digit > 9:
  is_error = True
  print('Invalid digit.')

if not is_error:
  while num > 0:
    if digit == num % 10:
      times += 1
    num //= 10

  print(f'Digit {digit} occurs {times} {"times" if times == 0 or times > 1 else "time"}.')