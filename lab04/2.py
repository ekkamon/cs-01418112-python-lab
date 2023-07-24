totalPrice = -1
foodName = ''
isSelectMainMenu = True

print('---<< Main Menu >>---')
print(f'{"":4}<B>urger Meal')
print(f'{"":4}<C>hicken Meal')
print(f'{"":4}<P>asta Meal')

mainMenu = str(input('Enter your choice: '))

if mainMenu == 'B' or mainMenu == 'b':
    print('---<< Burger Sub Menu >>---')
    print(f'{"":4}<R>egular Burger')
    print(f'{"":4}<C>heese Burger')
    print(f'{"":4}<D>ouble Cheese Burger')
    
    subMenu = str(input('Enter your choice: '))
    
    if subMenu == 'R' or subMenu == 'r':
        foodName = 'Regular Burger'
        totalPrice = 60
    elif subMenu == 'C' or subMenu == 'c':
        foodName = 'Cheese Burger'
        totalPrice = 75
    elif subMenu == 'D' or subMenu == 'd':
        foodName = 'Double Cheese Burger'
        totalPrice = 90
    
elif mainMenu == 'C' or mainMenu == 'c':
    print('---<< Chicken Sub Menu >>---')
    print(f'{"":4}<F>ried Chicken')
    print(f'{"":4}<G>rilled Chicken')
    print(f'{"":4}<C>hef\'s Chicken')
    
    subMenu = str(input('Enter your choice: '))
    
    if subMenu == 'F' or subMenu == 'f':
        foodName = 'Fried Chicken'
        totalPrice = 120
    elif subMenu == 'G' or subMenu == 'g':
        foodName = 'Grilled Chicken'
        totalPrice = 150
    elif subMenu == 'C' or subMenu == 'c':
        foodName = 'Chef\'s Chicken'
        totalPrice = 180
        
elif mainMenu == 'P' or mainMenu == 'p':
    print('---<< Pasta Sub Menu >>---')
    print(f'{"":4}<S>paghetti de Italiano')
    print(f'{"":4}<L>asagna Supreme')
    print(f'{"":4}<M>acaroni Special')
    
    subMenu = str(input('Enter your choice: '))
    
    if subMenu == 'S' or mainMenu == 's':
        foodName = 'Spaghetti de Italiano'
        totalPrice = 90
    elif subMenu == 'L':
        foodName = 'Lasagna Supreme'
        totalPrice = 120
    elif subMenu == 'M':
        foodName = 'Macaroni Special'
        totalPrice = 100    
else:
    isSelectMainMenu = False
    print('Invalid main menu choice.')
   
  
if isSelectMainMenu and totalPrice == -1:
    print('Invalid sub menu choice.')
elif totalPrice > 0:
    print(f'Your {foodName} is {totalPrice} Baht.')