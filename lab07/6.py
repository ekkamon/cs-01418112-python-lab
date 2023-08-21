height = int(input('Enter height: '))
width = int(input('Enter width: '))

def print_star(txt, width):
    x = 0
    
    while x < width:
        print(txt, end = '')        
        x += 1


if height <= 0 or width <= 0:
    print('Invalid input, program terminates.')
else:
    i = 1
    
    while i <= height:
        print_star('* ' if i % 2 > 0 else ' *', width)
        print()
        
        i += 1