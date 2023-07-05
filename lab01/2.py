s1 = int(input('Enter your exercise time 1: '))
s2 = int(input('Enter your exercise time 2: '))

total = s1 + s2

h = total // 3600
m = total % 3600 // 60
s = total % 3600 % 60

print('It', 'is', h, 'hours', m, 'minutes and', s, 'seconds.')