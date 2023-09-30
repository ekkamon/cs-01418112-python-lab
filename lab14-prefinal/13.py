num = str(input())

data = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def is_numberic(num):
    for val in num:
        if ord(str(val)) < 48 or ord(str(val)) > 57:
            return False
        
    return True

def to_speech_tens(num):
    tens = (num // 10) * 10
    units = num % 10
    
    if num <= 20:
        return data[num]
    elif units > 0:
        return f'{data[tens]}-{data[units]}'
    else:
        return f'{data[tens]}'
    
def to_speech_hundreds(num):
    hundreds = num // 100
    
    if num % 100 > 0:
        return f'{data[hundreds]}-hundred-{to_speech_tens(num  % 100)}'
    else:
        return f'{data[hundreds]}-hundred'

if not num or len(num) > 3 or not is_numberic(num):
    print('ERROR')
else:
    num = int(num)
    
    if len(str(num)) <= 2:
        print(to_speech_tens(num))
    else:
        print(to_speech_hundreds(num))