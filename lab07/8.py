c = int(input())

count = 0

_min = ((2**32) - 1)
_max = -1 * ((2**32) - 1)

a = 1

while a <= c-1:
    b = 1
    
    while b <= c-1:
        if (a ** 2) + (b ** 2) == c**2:
            print(a, b)
            if a < _min and b > _max:
                print('asdasd, a, b')
                if a < _min:
                    _min = a
                    
                if b > _max:
                    _max = b
                    
                count += 1
        b += 1
    a += 1
    
print(count)