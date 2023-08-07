_max = 0
count = 0

while True:
    h = int(input())
    
    if h == -1:
        break
    
    if h > _max:
        _max = h
        count += 1
        
print(count)