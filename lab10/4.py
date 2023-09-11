scores = []

def find_mode(target, l):
    count = 0
    
    for val in l:
        if count > 1:
            break
        
        if target == val:
            count += 1
        
    return True if count > 1 else False

while len(scores) < 20:
    score = int(input('Enter score: '))
    
    if score < 0 or score > 10:
        print('Score is out of range.')
        continue
    
    scores.append(score)
    
print('-----')
print('Original list:')
print(scores)
print('Mode of scores:')

cache = []  

for target in scores:
    if target in cache:
        continue
    
    if find_mode(target, scores) == True:
        print(target)
        cache.append(target)