majors = str(input()).split(',')
target = int(input())

majors.pop()

print(majors[(target % len(majors)) - 1])