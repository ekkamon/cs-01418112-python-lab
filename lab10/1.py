original_scores = []

def find_score(target, _list):
    count = 0
    
    for val in _list:
        if val == target:
            count += 1
            
    return count

while len(original_scores) < 20:
    score = int(input('Enter score: '))
    
    if score < 0 or score > 10:
        print('Score is out of range.')
        continue
    
    original_scores.append(score)

print('Original list:')
print(original_scores)

for target in range(0, 11):
    print(f'{target:>2d} {"*" * find_score(target, original_scores)}')