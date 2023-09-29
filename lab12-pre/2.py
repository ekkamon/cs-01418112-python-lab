_max = 0
result = ''

while True:
  text = str(input())

  if text == "":
    break

  if len(text) > _max:
    _max = len(text)
    result = text

print(result)