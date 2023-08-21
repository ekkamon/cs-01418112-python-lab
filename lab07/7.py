num = int(input('Enter positive integer: '))


def is_prime(number):
    count = 0
    i = 1
    
    while i <= number:
        if number % i == 0:
            count += 1
            
        i += 1
        
    return True if count == 2 else False
    
if num < 1:
    print('Invalid number.')
elif num == 1:
    pass
else:
    i = 2
    
    while i <= num:
        if num % i == 0 and is_prime(i):
            print(i)
            num //= i
        else:
            i += 1