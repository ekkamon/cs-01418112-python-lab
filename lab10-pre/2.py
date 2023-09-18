# 1
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
i = 0
total = 0

while i < 10:
    total += primes[i]
    i += 1
    
print(total)

# 2
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i = 0

while i < 12:
    print(months[i], days_in_month[i])
    i += 1

