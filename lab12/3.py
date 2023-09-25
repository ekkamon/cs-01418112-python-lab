data = []

def get_equal_idx():
    _max = 0
    
    for val in data:
        idx_equal = val.find('=')
        
        if idx_equal > _max:
            _max = idx_equal
    
    return _max

def set_space_between_equal(text):
    result = ''
    equal_idx = text.find('=')
    
    for idx in range(len(text)):
        val = text[idx]
        
        result += val
        
        if idx == equal_idx - 1 and val != ' ':
            result += ' '
            
    return result

while True:
    text = str(input())
    
    if text == '-1':
        break
    
    data.append(text)

equal_idx = get_equal_idx()

for val in data:
    val = set_space_between_equal(val)    