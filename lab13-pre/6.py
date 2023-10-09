data = []

while True:
    text = str(input())
    
    if text == '':
        break
    
    data.append(text)
    
print("".join(data))