target = 72

guessNum = int(input('Enter your guess (0 - 100): '))

if target == guessNum:
    print('Congratulations, your guess is correct.')
elif guessNum < 0 or guessNum > 100:
    print('Sorry, out of range, try again later.')
else:
    print('Sorry, your guess is wrong, try again later.')