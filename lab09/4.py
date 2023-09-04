n = int(input("Enter n: "))

def factorial(num):
    _sum = 1
    
    if num == 0 or num == 1:
        return _sum
    
    i = 1
    
    while i <= n:
        _sum *= i
        i += 1
        
    return _sum

print(f'{n}!', '=', factorial(n))