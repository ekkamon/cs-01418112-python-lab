def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    i = 1
    before = 1
    last = 1
    
    while i <= (n - 2):
        value = before + last
        before = last
        last = value
        i += 1
        
    return value
        
n = int(input("Enter n: "))
print('fibo({:d}) = {:d}'.format(n, fibo(n)))