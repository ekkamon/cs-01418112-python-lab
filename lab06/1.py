target = int(input('Enter a target (4-digit integer): '))
guess = int(input('Enter your guess (4-digit integer): '))

target_length = target
guess_length = guess
position = 0
digits = 0

if target == guess:
    print('Congratulations, you just mastered my mind!!')
else:
    while target_length > 0:
        target_value = target_length % 10
        guess_value = guess_length % 10

        if guess_value == target_value:
            position += 1
        else:
            num = guess
            while num > 0:
                num_value = num % 10

                if num_value == target_value:
                    digits += 1

                num //= 10
            

        target_length //= 10
        guess_length //= 10

    position_number = ''
    digits_number = ''
    
    if position == 0:
        position_number = 'No'
    elif position == 1:
        position_number = 'One'
    elif position == 2:
        position_number = 'Two'
    elif position == 3:
        position_number = 'Three'
    else:
        position_number == 'Four'
        
    if digits == 0:
        digits_number = 'no'
    elif digits == 1:
        digits_number = 'one'
    elif digits == 2:
        digits_number = 'two'
    elif digits == 3:
        digits_number = 'three'
    else:
        digits_number == 'four'
            
    print(f'{position_number}', end=' ')
    
    if position == 0 or position > 1:
        print('positions', end = ' ')
    else:
        print('position', end = ' ')


    print('correct,', end= ' ')
    print(f'{digits_number}', end=' ')
    
    if digits == 0 or digits > 1:
        print('digits', end = ' ')
    else:
        print('digit', end = ' ')
    
    print('correct')