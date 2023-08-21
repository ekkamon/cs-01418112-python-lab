total = int(input())
count = 0

def check(a, b):
    return a**2 + b**2 == total**2

def find(start_scope, end_scope):
    i = start_scope
    while i <= end_scope:
        x = start_scope
        while x <= end_scope:
            if check(i, x):
                return i, x
            x += 1
        i += 1
        
    return False

start = 1
end = total - 1

while True:
    result = find(start, end)

    if result == False:
        break

    a, b = result

    count += 1

    start = a + 1
    end = b - 1

print(count)