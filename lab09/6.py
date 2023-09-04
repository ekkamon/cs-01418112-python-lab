def alternating_sum(num):
    i = 2
    total = 1
    
    while i <= num:
        if i % 2 > 0:
            total += i
        else:
            total -= i
            
        i += 1
        
    return total

n = int(input("Enter n of series: "))

print("Alternating Sum from 1 to {:d} is {:d}".format(n, alternating_sum(n)))