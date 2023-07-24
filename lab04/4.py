country = str(input('Enter your buffet choice: '))

price = 0

if country == 'Korean':
    price = 1500
elif country == 'Japanese':
    price = 1000
else:
    price = -1
    
if price == -1:
    print(f'Sorry, there is no {country} buffet.')
else:
    isWednesday = str(input('Is today Wednesday (yes/no)? '))
    
    if isWednesday == 'yes':
        price = price * (85/100)
    
    print(f'Your payment is {price:.2f} Baht.')        
    