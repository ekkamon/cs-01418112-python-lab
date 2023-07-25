height = int(input('Enter height: '))

start_space = 0
middle_space = 3

i, x = 0, 0

while i < height:
  if i > 0:
    start_space += 2
    
  i += 1

while x < height:
  txt = ''

  if x == 0:
    txt = '1'
  else:
    txt = f'1{" " * middle_space}1'
    middle_space += 4

  print(f'{" " * start_space}{txt}')
  start_space -= 2
  x += 1