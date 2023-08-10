frames = 1
score = 0

while frames <= 10:
    count = 1
    
    print(f'Frame # {frames}')
    firstPinsDown = int(input('  Number of pins down: '))
    
    if firstPinsDown == 10:
        score += 10
        pass
    else:
        leftPins = 10 - firstPinsDown
        
        print(f'Frame # {frames}')
        secondPinsDown = int(input(f'  Number of pins down (0-{leftPins}): '))

        if secondPinsDown == leftPins:
            score += 10
        else:
            score += firstPinsDown + secondPinsDown
    
    frames += 1

print(f'Total score is {score}')