def get_inputs():
    arr = []
    
    while True:
        num = int(input())
        
        if num == 0:
            break
        
        arr.append(num)
        
    return arr
        
def get_sum(arr):
    _max = sum(arr)
    
    for i in range(len(arr)):
        total = arr[i]
        
        for x in range(i+1, len(arr)):
            total += arr[x]
            
            if total > _max:
                _max = total
                
    return _max

def main():
    print(get_sum(get_inputs()))
        
main()