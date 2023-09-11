import math

scores = []
count = 0

def avg(_list):
    return sum(_list) / count

def find_sd(l):
    total = 0
    
    for val in l:
        total += (val - avg(l)) ** 2
        
    return math.sqrt(total / (len(l) - 1))
    
while True:
    score = float(input('Enter score: '))
    
    if score == -1:
        break
    
    if score < 0 or score > 100:
        print('Score is out of range.')
        continue
    
    scores.append(score)
    count += 1
    
if len(scores) > 0:
    print(f'Maximum score is {max(scores):.2f}.')
    print(f'Minimum score is {min(scores):.2f}.')
    print(f'Average score is {avg(scores):.2f}.')
    print(f'Standard deviation is {find_sd(scores):.2f}.')    
