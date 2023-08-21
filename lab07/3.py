num = int(input('Enter a number: '))

#pre-defined function:
def change_to_abc(number):
    result = ''
    i = 0
    
    while i < number:
        result += chr(ord('A') + i)
        i += 1
        
    return result

if num <= 0 or num > 26:
    print('Invalid input, program terminates.')
else:
    i = 1
    
    while i <= num:
        print(change_to_abc(i))
        i += 1
        
    i = num - 1
    
    while i > 0:
        print(change_to_abc(i))
        i -= 1