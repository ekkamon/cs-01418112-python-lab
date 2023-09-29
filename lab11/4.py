target = str(input())
count = 0

inUse = []
    
def isUse(target):
    for i in range(len(inUse)):
        val = inUse[i]
        
        if target == val:
            return True
        
    return False
 
while True:
    text = str(input())
    
    if text == '0':
        break
    
    if isUse(text):
        continue
    
    inUse.append(text)
    
    for i in range(len(target)):
        val = target[i]
        
        if text == val:
            count += 1
        
print(f'{count}/{len(target)}')