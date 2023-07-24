age = int(input('Enter your age: '))
income = float(input('Enter your net income: '))

if age < 15 or age > 60:
    print('Invalid age.')
else:
    if income > 79_999 or income < 1:
        print('Invalid income.')
    else:
        total = income
        
        if income >= 1 and income <= 30_000:
            total = total * (20/100)
        else:
            total = (30_000 - total) * (8/100)
        
    print(f'Your negative income tax is {total:.2f} Baht.')
        