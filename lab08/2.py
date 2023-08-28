def digit(n):
    return n % 10

def tens(n):
    return n % 100 // 10

def hundreds(n):
    return n % 1000 // 100

def thousands(n):
    return n % 10_000 // 1000

def sum_digits(n):
    _sum = 0
    num = n
    
    while num > 0:
        value = num % 10
        _sum += value
        num //= 10
        
    return _sum

n = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))