def check(source, target):
    position = 0
    digits = 0
    
    source_used = []
    target_used = []
    
    # check position
    for i in range(len(source)):
        if source[i] == target[i]:
            source_used.append(i)
            target_used.append(i)
            position += 1
    
    # check duplicate
    for i in range(len(source)):
        if i in source_used:
            continue
        
        for j in range(len(target)):          
            if source[i] == target[j] and j not in target_used:
                digits += 1
                source_used.append(i)
                target_used.append(j)
                break
            
    return f'{position}-{digits}'
    

def main():
    source = str(input())
    target = str(input())
    
    print(check(source, target))

main()