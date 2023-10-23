def get_fibo(end, isEvent):
  last = 0
  now = 1
  events = []
  odds = []
  
  for i in range(end+1):
    if i % 2 == 0:
      events.append(now)
    else:
      odds.append(now)
    
    _last = last
    last = now
    now = now + _last
    
  return sum(events if isEvent else odds)

    
def main():
  num = int(input())
  target = str(input()).upper()

  if num < 0 or target not in ['O', 'E'] or (num == 0 and target == 'O'):
    print('ERROR')
    return
  
  print(get_fibo(num, target == 'E'))
    
main()