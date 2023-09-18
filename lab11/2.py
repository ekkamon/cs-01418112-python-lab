text = str(input())

vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for val in text:
    if val.lower() in vowel:
        count += 1
        
print(count)