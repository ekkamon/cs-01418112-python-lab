def get_inputs():
    target = str(input())
    arr = []
    
    while True:
        data = str(input())
        
        if data == '0':
            break
        
        arr.append(data)
        
    return target, arr 
    
def main():
    target, arr = get_inputs()
    answer = ''
    
    for val in target:
        if val in arr:
            answer += val
        else:
            answer += '-'
            
    print(answer)
    
main()