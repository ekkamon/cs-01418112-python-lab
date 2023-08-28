# sec 1

def f1(a, b):
    i = a
    count = 0

    while i > 0:
        value = i % 10
        
        if value >= b:
            count += 1
            
        i //= 10
        
    return count


# sec 2
a = int(input())
b = int(input())

print(f1(b, a))