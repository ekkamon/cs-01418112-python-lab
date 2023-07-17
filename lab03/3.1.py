c = float(input())
char = str(input())


if char == 'F' or char == 'f':
    print(((9/5) * c) + 32)
elif char == 'K' or char == 'k':
    print(c + 273.15)
else:
    print('ERROR')