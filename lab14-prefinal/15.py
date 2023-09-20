text = str(input()).split(' ')

def is_except(target):
  data = ['for', 'and', 'with', 'of']

  if target.lower() in data:
    return True

  return False

for i in range(len(text)):
  val = text[i]

  if len(val) > 0 and not is_except(val):
    text[i] = val[0].upper() + val[1:]

print(' '.join(text))