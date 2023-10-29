import math

def get_inputs():
    count = int(input())
    arr = []
    
    for _ in range(count):
        arr.append(int(input()))
                   
    return arr

def find(arr):
    _min = math.inf
    result = []
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            value = abs(arr[i] - arr[j])
            
            if value <= _min:
                _min = value
                result.append([arr[i], arr[j]])
    
    for val in result:
        diff = abs(val[0] - val[1])
        
        if diff == _min:
            val.sort()
            print(val[0], val[1])
    
def main():
    inputs = get_inputs()
    find(inputs)
    
main()