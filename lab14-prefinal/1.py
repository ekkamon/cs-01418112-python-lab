text = str(input())

data = []

# if can't use method lower()
def toLowerCase(text):
  total = ""

  for val in text:
    ascii_val = 32 if ord(val) < 97 else 0

    total += chr(ord(val) + ascii_val)

  return total


for i in range(len(text)):
  if i == len(text) - 1:
    break

  merge_txt = toLowerCase(text[i] + text[i+1])

  if merge_txt in data:
    continue

  data.append(merge_txt)

data.sort()

for val in data: print(val)