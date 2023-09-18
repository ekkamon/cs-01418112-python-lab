text = str(input())

vowel = ['a', 'e', 'i', 'o', 'u']
new_text = ''

for val in text:
    if val.lower() in vowel:
        continue
    
    new_text += val
    
print(new_text)