def extract_string(text):
    if text == '':
        return []
    
    result = ''

    for idx in range(len(text)):
        val = text[idx]

        if val.isdigit():
            before_is_digit = text[idx-1:idx].isdigit()
            after_is_digit = text[idx+1:idx+2].isdigit()

            if not before_is_digit and not after_is_digit:
                result += f'|{val}|'
                continue

            if not before_is_digit:
                result += f'|{val}'
                continue
            
            if not after_is_digit:
                result += f'{val}|'
                continue
        
        result += val

    if result[0] == '|':
        result = result[1:]
    
    if result[-1] == '|':
        result = result[:-1]

    return [int(val) if val.isdigit() else val for val in result.split('|')]