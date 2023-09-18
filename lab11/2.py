text = str(input())

vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in range(len(text)):
    val = text[i]
    
    if val.lower() in vowel:
        count += 1
        
print(count)