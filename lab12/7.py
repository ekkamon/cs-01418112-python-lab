text = str(input())

sep = [' ', '-', '_', '=', '.', '$']

def split_words(text):
  target = ''

  for val in text:
    if val in sep:
      target += '|'
      continue

    target += val

  return target.split('|')

def set_camel_case(data):
  idx = 0
  result = ''

  for val in data:
    if len(val) < 1:
      continue

    if idx == 0:
      result += val.lower()
    else:
      result += val[0].upper() + val[1:].lower()

    idx += 1

  return result

data = split_words(text)

if len(data) < 2:
  print(text)
else:
  print(set_camel_case(data))