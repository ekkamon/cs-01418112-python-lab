target = int(input('Enter a target (4-digit integer): '))
guess = int(input('Enter your guess (4-digit integer): '))

save_target = target

pos = 0
digits = 0

if target == guess:
    print('Congratulations, you just mastered my mind!!')
else:
    while target > 0:
        target_value = target % 10
        guess_value = guess % 10
        
        if target == 0 or guess == 0:
            break
        
        target //= 10
        guess //= 10
        
        if target_value == guess_value:
            pos += 1
        else:
            new_target = save_target
            
            while new_target > 0:
                value = new_target % 10
                
                if new_target == 0:
                    break
                
                if guess_value == value:
                    digits += 1
                
                new_target //= 10
        
    pos_str = ''
    digit_str = ''
    
    if pos == 0:
        pos_str = 'No'
    elif pos == 1:
        pos_str = 'One'
    elif pos == 2:
        pos_str = 'Two'
    elif pos == 3:
        pos_str = 'Three'
    else:
        pos_str == 'Four'
        
    if digits == 0:
        digit_str = 'no'
    elif digits == 1:
        digit_str = 'one'
    elif digits == 2:
        digit_str = 'two'
    elif digits == 3:
        digit_str = 'three'
    else:
        digit_str == 'four'
            
    print(f'{pos_str} {"positions" if pos > 1 or pos == 0 else "position"} correct, {digit_str} {"digits" if digits > 1 or digits == 0 else "digit"} correct')