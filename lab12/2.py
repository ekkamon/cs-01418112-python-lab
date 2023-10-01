text = str(input())

def get_target_data(text):
    data = []
    result = ''
    
    for val in text:
        if val == ',':
            data.append(result)
            result = ''
            continue
        
        result += val
        
    if text[-1] == ',':
        data.append('')
    else:
        data.append(text[-1])
        
    return data

def clean_space(data):
    arr = []
    
    for val in data:
        while len(val) > 0 and val[0] == ' ':
            val = val[1:]
            
        while len(val) > 0 and val[-1] == ' ':
            val = val[:-1]
        
        arr.append(val)
    return arr
    
text = get_target_data(text)
text = clean_space(text)

for idx in range(len(text)):
    val = text[idx]
    
    print(f'"{val}"', end='')
    
    if idx != len(text) -1:
        print(',', end='')
    