hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))

if hours < 0 or minutes < 0 or minutes >= 60:
    print('Input Error!')
else:
    total = 0
    
    minutes += hours * 60
    
    if minutes <= 15:
        total = 0
    else:
        hours = minutes // 60
        
        
        if minutes % 60 > 0:
            hours += 1
            
        if (hours - 2 >= 0):
            hours -= 2
            total = 10 + (hours * 10)
        else:
            total = 10        
        
    if total == 0:
        print('No charge, thanks.')
    else:
        print('Total amount due is {:d} Bahts.'.format(total))
