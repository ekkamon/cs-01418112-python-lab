import math

def get_min_value():
    _min = math.inf
    
    for val in data:
        if val < _min:
            _min = val
            
    return _min
    
data = []

while True:
    num = str(input())
    
    if num == '':
        break

    data.append(float(num))

print(data.count(get_min_value()))