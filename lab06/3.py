first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

output_first = first
output_second = second

gcd = (2**31) - 1
lcm = 0

while True:
  if second == 0:
    break

  divide = first % second
  first = second
  second = divide

  print(first, second)

  if divide < gcd and divide != 0:
    gcd = divide


print(f'  >> gcd({output_first}, {output_second}) ={gcd:>7d}')
# print(f'  >> lcm({output_first}, {output_second}) ={gcd:>7d}')