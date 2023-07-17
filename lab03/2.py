amount = float(input('Enter buying amount: '))

if amount >= 3000:
    amount *= (85/100)
elif amount >= 1000:
    amount *= (90/100)
    
print('Amount due after discount is {:.2f} baht.'.format(amount))