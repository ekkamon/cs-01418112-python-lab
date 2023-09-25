idx = 1
result = ''

while True:
  text = str(input())

  if text == "":
    break
  
  if idx % 2 > 0:
    result += max(text)
  else:
    result += min(text)
  
  idx += 1
  
print(result)

