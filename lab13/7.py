def get_bomb_positions(count):
  data = []

  for _ in range(count):
    y, x = str(input()).split(',')
    data.append([int(y), int(x)])

  return data

def assign_pattern(table, x, y, height, width):
  for _y in range(y-1, y+2):
    for _x in range(x-1, x+2):
      if (_y < 0 or _x < 0) or (_y > (height - 1) or _x > (width - 1)):
        continue
      
      if not str(table[_y][_x]).isdigit():
        continue
      
      table[_y][_x] += 1
      
  return table

def create_table(height, width, bomb_positions):
  table = [[0] * width for _ in range(height)]
  
  for y, x in bomb_positions:
    table[y][x] = '*'
    assign_pattern(table, x, y, height, width)
    
  return table

def main():
  height, width = [int(val) for val in str(input()).split('x')]
  bomb_positions = get_bomb_positions(int(input()))
  table = create_table(height, width, bomb_positions)
  
  for val in table:
    print(''.join([str(val) for val in val]))
  
main()