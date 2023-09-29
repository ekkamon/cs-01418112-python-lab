text = str(input())

vowel = ['a', 'e', 'i', 'o', 'u']
result = ''

for val in text:
    if val.lower() in vowel:
        result += val.upper()
    else:
        result += val.lower()
        
print(result)