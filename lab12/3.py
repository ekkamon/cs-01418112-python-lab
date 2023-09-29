data = []

def get_data_between_equal(text):
    idx = text.find('=')
    start, end = text[:idx].strip(), text[idx+1:].strip()

    return start, end

def get_equal_idx():
    _max = 0
    
    for val in data:
        idx_equal = val.find('=')
        
        if idx_equal > _max:
            _max = idx_equal
    
    return _max
    
def set_space_format(text):
    start, end = get_data_between_equal(text)
    space_size = (get_equal_idx()) - (len(start)) -1

    return f'{" " * space_size}{start} = {end}'

while True:
    text = str(input())
    
    if text == '-1':
        break

    start, end = get_data_between_equal(text)
    
    data.append(f'{start} = {end}')

for val in data:
    print(set_space_format(val))