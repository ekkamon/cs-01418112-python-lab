frames = 1
score = 0

while frames <= 10:
    count = 1
    
    print(f'Frame # {frames}')
    
    pinsDown = int(input('Number of pins down: '))
    
    if pinsDown == 10:
        score += 10
        pass
    else:
        pinsDown = int(input(f'Number of pins down (0-{10-pinsDown}): '))
        
        
    
    frames += 1
    