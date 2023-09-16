scores = []

def get_max_mode_value():
    _max = -1
    
    for val in scores:
        count = scores.count(val)
        if count > _max:
            _max = count
            
    return _max
            
def find_mode():
    modes = []
    mode_max_value = get_max_mode_value()
    
    for val in scores:
        if val in modes:
            continue
        
        if val not in modes and scores.count(val) == mode_max_value:
            modes.append(val)
            
    return modes
        
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

modes = find_mode()
modes.sort()

for val in modes: print(val)