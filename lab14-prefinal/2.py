father = str(input())
mother = str(input())

vowel = ['a', 'e', 'i', 'o', 'u']

def find_vowel(text):
  data = []

  for i in range(len(text)):
    if text[i] in vowel:
      data.append(i)

  return data

def get_father_name():
  idxes = find_vowel(father)

  if len(idxes) < 2:
    return father
  
  return father[:idxes[1]]

def get_mother_name():
  idxes = find_vowel(mother)

  if len(idxes) < 1:
    return mother

  return mother[idxes[0]+1:]

print(get_father_name() + get_mother_name())

