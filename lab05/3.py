count = 0

while True:
  number = int(input('Enter number: '))

  if number < 0:
    break

  if number % 2 > 0:
    count += 1

print(f'Received {count} odd numbers')