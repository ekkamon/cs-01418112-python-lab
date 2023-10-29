def find_ammo(zombies, damage):
  arr = []
  ammo = 0
  
  for hp in zombies:
    value = hp // damage if hp % damage == 0 else (hp // damage) + 1
    ammo += value
    arr.append(ammo)

  print(ammo)
  print(' '.join([str(val) for val in arr]))
    
def main():
  damage = int(input())
  zombies = [int(val) for val in str(input()).split(' ')]
  
  find_ammo(zombies, damage)
  
main()