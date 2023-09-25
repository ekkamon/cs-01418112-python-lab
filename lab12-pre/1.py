_max = 0

while True:
  text = str(input())

  if text == "":
    break

  if len(text) > _max:
    _max = len(text)

print(_max)