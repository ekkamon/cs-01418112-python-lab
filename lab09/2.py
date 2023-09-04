def factor_count(n):
    count = 0
    i = 1
    
    while i <= n:
        if n % i == 0:
            count += 1
        
        i += 1
            
    return count

n = int(input("Enter n: "))
c = factor_count(n)
print(c)


