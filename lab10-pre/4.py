# 1
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
total = 0

for val in primes:
    total += val
    
print(total)

# 2
import math

def find_max(list):
    _max = -math.inf
    
    for val in list:
        if val > _max:
            _max = val
            
    return _max

print(find_max([1, 2, 3, 4]))
print(find_max([4, 3, 2, 1]))
print(find_max([4, 3, 5, 9, 7, 2, 4, 4, 10, 0, 11, 8]))
print(find_max([-7, -9, -8, -2, -7, -11, -4, -5]))