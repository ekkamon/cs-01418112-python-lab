first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

output_first = first
output_second = second

gcd = (2**31) - 1

while True:
  if second == 0:
    break

  divide = first % second
  first = second
  second = divide

  if divide < gcd and divide != 0:
    gcd = divide
    
if gcd == (2**31) -1:
  gcd = 1

lcm = int((output_first * output_second) / gcd)

print(f'  >> gcd({output_first}, {output_second}) ={gcd:>7d}')
print(f'  >> lcm({output_first}, {output_second}) ={lcm:>7d}')