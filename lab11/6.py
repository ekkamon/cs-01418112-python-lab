text = str(input())

def is_vowel(target):
  vowel = ['a', 'e', 'i', 'o', 'u']

  for i in range(len(vowel)):
    if vowel[i] == target:
      return True
    
  return False

i = 0

while i < len(text):
  val = text[i]

  print(val, end='')

  if len(text[i:i+2]) < 2:
    break
  
  if is_vowel(val) and text[i+1] == 'p' and text[i+2] == val:
    i += 3
  else:
    i += 1