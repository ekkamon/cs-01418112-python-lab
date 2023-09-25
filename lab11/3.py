text = str(input())

vowel = ['a', 'e', 'i', 'o', 'u']
new_text = ''

for i in range(len(text)):
    val = text[i]
    
    if val.lower() in vowel:
        continue
    
    new_text += val
    
print(new_text)