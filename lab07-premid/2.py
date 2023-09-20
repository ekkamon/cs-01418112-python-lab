print('Upper left corner coordinate:')
block_x = int(input('  << x axis: '))
block_y = int(input('  << y axis: '))
block_w = int(input('  << Eastern: '))
block_h = int(input('  << Southern: '))
print('Enter a coordinate:')
target_x = int(input('  << x axis: '))
target_y = int(input('  << y axis: '))

is_inside = False

if (target_x >= block_x and target_x <= block_x + block_w) and (target_y >= block_y - block_h and target_y <= block_y):
  is_inside = True

print(f'>>> ({target_x:.2f}, {target_y:.2f}) {"is" if is_inside else "is not"} inside the rectangle.')