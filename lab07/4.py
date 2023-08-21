num = int(input('Enter a number: '))

def print_factorial(number):
    total = 1
    
    if number >= 0 and number <= 1:
        print(f'{number}! = 1 = 1')
    else:
        i = number
        
        print(f'{number}! = ', end='')
        
        while i > 0:
            total *= i
            
            if i == 1:
                print(1, end=' ')
            else:
                print(i, end=' x ')
            i -= 1
            
        print(f'= {total}')

if num < 0:
    print('Invalid input, program terminates.')
else:
    i = 0
    
    while i <= num:
        print_factorial(i)
        i += 1