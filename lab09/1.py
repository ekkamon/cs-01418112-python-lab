def check_prime(n):
    count = 0
    i = 1
    
    while i <= n:
        if n % i == 0:
            count += 1
            
        i += 1
        
    return True if count == 2 else False

n = int(input("Enter number: "))

if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")