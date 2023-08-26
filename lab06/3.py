import math

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

first_value = first
second_value = second

gcd = math.inf

while True:
  if first == 0 or second == 0:
    break

  divide = first % second

  first = second
  second = divide

  if first != 0 and first < gcd:
    gcd = first

  if second != 0 and second < gcd:
    gcd = second

lcm = int(abs(first_value * second_value) / gcd)

print(f'  >> gcd({first_value}, {second_value}) ={gcd:>7d}')
print(f'  >> lcm({first_value}, {second_value}) ={lcm:>7d}')