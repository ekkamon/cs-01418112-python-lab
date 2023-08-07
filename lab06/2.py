target = 72
count = 0

while True:
    guess = int(input('Enter your guess: '))
    
    count += 1
    
    if target == guess:
        print('Congratulations, your guess is correct.')
        print(f'Total number of guesses is {count}.')
        break
    
    if guess < 0 or guess > 100:
        print('Sorry, your guess is out of range.')
        continue
    
    if guess < target:
        print('Sorry, your guess is too low.')
        continue
    elif guess > target:
        print('Sorry, your guess is too high.')
        continue