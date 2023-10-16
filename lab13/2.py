count = int(input())
arr = [input().split(' ') for _ in range(count)]

def get_value(card):
  if card.isdigit():
    return int(card)
  else:
    if card in ['J', 'Q', 'K']:
      return 10
    else:
      return 1

for cards in arr:
  score = 0
  
  for val in cards:
    if score > 16:
      break
    
    score += get_value(val)
    
  print(score if score <= 21 else 'busted')
