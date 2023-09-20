text = str(input())

data = []

for i in range(len(text)):
  if i == len(text) - 1:
    break

  merge_txt = (text[i] + text[i+1]).lower()

  if merge_txt in data:
    continue

  data.append(merge_txt)

data.sort()

for val in data: print(val)