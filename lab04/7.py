pokemon_level = int(input('Enter level pokemon: '))
pokeball_level = str(input('Enter level pokeball: '))
distance = int(input('Enter distance: '))

quality = 0.0

if pokeball_level == 'L' or pokeball_level == 'l':
    if pokemon_level >= 61:
      quality = 0.1
    elif pokemon_level >= 41:
      quality = 0.03
    else:
      quality = 0.05
elif pokeball_level == 'M' or pokeball_level == 'm':
    if pokemon_level >= 61:
      quality = 0.08
    elif pokemon_level >= 41:
      quality = 0.05
    else:
      quality = 0.03
    
elif pokeball_level == 'H' or pokeball_level == 'h':
    if pokemon_level >= 61:
      quality = 0.01
    elif pokemon_level >= 41:
      quality = 0.01
    else:
      quality = 0.01

result = 100 - (pokemon_level * distance * quality)

if result < 0:
  result = 0.0

print(f'{result:.2f} percent.')