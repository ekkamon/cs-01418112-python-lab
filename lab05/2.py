hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

if hours >= 0 and minutes > 0:
  hours += 1

if hours < 0 or hours > 20 or minutes < 0 or minutes > 59:
    print('Invalid time.')
else:
    if hours <= 2 or buyAmt >= 3001:
        print('No charge, thank you.')
    else:
        totalPrice = 0
        hours -= 2

        count = 3
        while hours > 0:
            if count >= 3 and count <= 4:
                if buyAmt < 300:
                  totalPrice += 20
            else:
                totalPrice += 50

            count += 1
            hours -= 1

        if totalPrice > 0:
            print(f'Total amount due is {totalPrice} Baht, thank you.')
        else:
            print('No charge, thank you.')
        