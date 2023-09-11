# 1
scores = []

scores.append(20)
print('Scores:', scores)
      
# 2
data = ['a', 'b', 'c', 'e', 'f']

data.append('d')
print('Data:', data)

# 3
def factors(number):
    factors = []
    for factor in range(1, number+1):
        if number % factor == 0:
            factors.append(factor)
    return factors

print('Factors of 27 is:', factors(27))

# 5
data = []

while True:
    num = int(input())
    
    if num == -1:
        break
    
    data.append(num)
    
print(data)

# 6
data = []

while True:
    txt = str(input())
    
    if txt == '':
        break
    
    data.append(txt)
    
print(data)