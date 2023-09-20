import math

while True:
  print('<<Point a>>')
  ax = int(input('Enter x coordinate: '))
  ay = int(input('Enter y coordinate: '))

  print('<<Point b>>')
  bx = int(input('Enter x coordinate: '))
  by = int(input('Enter y coordinate: '))

  if (ax == 0 and ay == 0) and (bx == 0 and by == 0):
    print('Goodbye')
    break

  horizon = 0
  vertical = 0

  i = ax
  while i != bx:
    if ax < bx:
      i += 1
    else:
      i -= 1

    horizon += 1

  i = ay
  while i != by:
    if ay < by:
      i += 1
    else:
      i -= 1

    vertical += 1

  print(f'Distance between ({ax}, {ay}) and ({bx}, {by}):')
  print(f'Euclidean distance is {math.sqrt(((ax - bx) ** 2) + ((ay - by) ** 2)):.2f}.')
  print(f'Horizontal distance is {horizon}.')
  print(f'Vertical distance is {vertical}.')

  direct = ''

  if (ax == bx) and (ay == by):
    direct = 'nowhere'
  elif ax == bx:
    if ay < by:
      direct = 'north'
    else:
      direct = 'south'
  elif ay == by:
    if ax > bx:
      direct = 'west'
    else:
      direct = 'east'
  elif ax > bx:
    if ay < by:
      direct = 'north-west'
    else:
      direct = 'south-west'
  elif ax < bx:
    if ay < by:
      direct = 'north-east'
    else:
      direct = 'south-east'

  print(f'We are going {direct}.')