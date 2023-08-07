num = int(input())

while True:
    target = 0
    
    if num < 10:
        print(num)
        break
    
    while num > 0:
        value = num % 10
        
        if num == 0:
            break
        
        target += value
        
        num //= 10
        
    num = target