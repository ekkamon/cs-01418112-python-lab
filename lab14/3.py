def get_variables():
    variables = {}
    
    print('Enter variables and values:')
    while True:
        data = str(input())
        
        if data == '-1':
            break
        
        key, value = [val.strip()  for val in data.split('=')]
        
        variables[key] = value
        
    return variables
        
def get_program():
    print('Enter your program:')
    
    arr = []
    
    
    while True:
        data = str(input())
        
        if data == '-1':
            break
        
        arr.append(data)
        
    return '|'.join(arr)
    
        
def print_result(variables, program):
    print('Result:')
    
    for key in variables:
        program = program.replace('{' + key + '}', variables[key])
        
    
    for val in program.split('|'):
        print(val)
    

def main():
    variables = get_variables()
    program = get_program()
    print_result(variables, program)

main()