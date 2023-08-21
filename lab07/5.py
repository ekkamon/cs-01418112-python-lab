def is_prime_number(number):
    count = 0
    i = 1
    
    while i <= number:
        if number % i == 0:
            count += 1
            
        i += 1
        
    return True if count == 2 else False

while True:
    num = int(input('Enter a number: '))
    
    if num == 0:
        print('End of program, goodbye.')
        break
    
    if num <= 1:
        print('Invalid input, try again.')
        continue
    
    if is_prime_number(num):
        print(f'{num} is a prime number.')
    else:
        print(f'{num} is not a prime number.')
