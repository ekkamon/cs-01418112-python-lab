n = int(input())

count = 0
moreThanForty = 0
totalScore = 0

while count < n:
  score = float(input())

  if score > 40.0:
    moreThanForty += 1

  totalScore += score

  count += 1

avg = totalScore / n

print(f'{avg:.2f}', moreThanForty)

  