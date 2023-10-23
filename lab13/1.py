def namelist(names):
  if len(names) == 0:
    return ''
  
  if len(names) == 1:
    return names[0]

  start = [names[idx] for idx in range(len(names) -1)]
  end = names[len(names)-1]

  return f'{", ".join(start)} & {end}'

print(namelist(['Bart', 'Viola', 'Peter', 'Nostel']))
print(namelist(['Bart', 'Viola']))
print(namelist(['Peter']))