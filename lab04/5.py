age = int(input('Enter your age: '))
income = float(input('Enter your net income: '))

if age < 15 or age > 60:
    print('Invalid age.')
else:
    total = 0

    if income > 79_999 or income < 1:
        print('Invalid income.')
    else:
        if income >= 1 and income <= 30_000:
            total = income * (20/100)
        else:
            extra = income - 30_000
            total = ((30_000 - extra) * (20/100)) + (extra * 8/100)
        
        print(f'Your negative income tax is {total:.2f} Baht.')
        