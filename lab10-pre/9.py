# 1
scores = [60, 70, 85, 66, 70, 0, 15, 9]
number_of_scores = len(scores)
print(number_of_scores)

# 2
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( 'There are', len(days), 'days in a week.' )

# 3
print(len([]))

# 4
scores = [60, 70, 85, 66, 70, 0, 15, 9]
total = sum(scores)
print(total)

# 5
scores = [60, 70, 85, 66, 70, 0, 15, 9]
max_score = max(scores)
print(max_score)

# 6
scores = [60, 70, 85, 66, 70, 0, 15, 9]
min_score = min(scores)
print(min_score)

# 7
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(min(days))

# 8
import math

data = []
target_idx = 0
_max = -math.inf

while True:
    txt = str(input())
    
    if txt == '':
        break
    
    data.append(txt)

for i in range(len(data)):
    if len(data[i]) > _max:
        target_idx = i
        
print(data[target_idx])