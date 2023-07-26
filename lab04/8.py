minutes = int(input('Minutes before due: '))
temp = float(input('Temperature: '))
is_raining = str(input('Is it raining (y/n)? '))

hours = minutes // 60
days = hours // 24

if hours % 24 >= 12:
  days += 1

is_asm = True

if days > 5:
  is_asm = False
elif days >= 2 and (temp > 40 or (temp > 25 and (is_raining == 'Y' or is_raining == 'y'))):
  is_asm = False

print(f'>>> {days} days before due.')

if is_asm :
  print('>>> I will do the assignment.')
else:
  print('>>> I will not do the assignment.')