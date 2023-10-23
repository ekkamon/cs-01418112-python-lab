def split_chemical(text): 
    #split data
    data = []
    string = ''
    
    for idx in range(len(text)):
        char = text[idx]
        
        if idx != 0 and char.isalpha() and char.isupper():
            data.append(string)
            string = ''
            
        string += char
    
    data.append(string)
    
    # split stuctures, values
    values = []
    stuctures = []
    
    for chemical in data:
        name, value = '', ''
        
        for char in chemical:
            if char.isalpha():
                name += char
            else:
                value += char
        stuctures.append(name)
        values.append(int(1 if value == '' else value))
        
    return stuctures, values


def find(text, target):
    if len(text) < 1 or len(target) < 1:
        return 0
    
    atom = 0
    
    stuctures, values = split_chemical(text)
    
    idx = 0
    for chemical in stuctures:
        if target == chemical:
            atom += values[idx]
            
        idx += 1
        
    return atom
        
def main():
    structure = str(input())
    target = str(input())

    print(find(structure, target))

main()