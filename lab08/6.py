import math

def sqrt_n_times(x, n):
    left = x
    i = n
    while i > 0:
        left = math.sqrt(left)
        i -= 1
        
    return left
    
x = float(input())
n = int(input())
print(sqrt_n_times(10**8, 3))