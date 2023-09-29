#section 1

text = str(input())

lower_count = 0
upper_count = 0

for val in text:
    if val.islower():
        lower_count += 1
    
    if val.isupper():
        upper_count += 1
        
print(lower_count)
print(upper_count)

#section 2

text = str(input())

for val in text:
    if val.islower():
        print(val.upper(), end='')
    else:
        print(val.lower(), end='')