_max = 0
data = []

while True:
    num = int(input())

    if num == -1:
        break
    
    if num > _max:
        _max = num
        data.append(num)
        
print(data)