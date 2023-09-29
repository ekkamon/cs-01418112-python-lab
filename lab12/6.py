text = str(input())

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
marks = ['.', ',', '-']

def is_currect_format():
    integer = ''
    decimal = ''
    
    data = text.split('.')
    
    if len(data) > 0: integer = data[0]
    if len(data) >= 2: decimal = data[1]
    
    # check decimal length
    if len(decimal) > 2:
        return False
    
    # check is digits
    for val in text:
        if val not in (digits + marks):
            return False
        
    integer_value = int(integer.replace(',', ''))
        
    if decimal != '':
        decimal_value = int(decimal)    
        
    # check comma
    if integer != f'{integer_value:,}' and integer != str(integer_value):
        return False
    
    total = str(integer_value) + ('.' if decimal != '' else '') + str(decimal)
    total = float(total) + 1
    
    return f'{float(total):.{len(decimal)}f}' if len(decimal) > 0 else int(total)
    
    
def main():
    answer = is_currect_format()
    print('ERROR' if answer == False else answer)
    
main()