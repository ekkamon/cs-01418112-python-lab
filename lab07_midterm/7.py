start_days = int(input())
target_days = int(input())

if (start_days > 0 and start_days <= 31) and (target_days > 0 and target_days <= 31) and start_days <= 8:
  target = target_days % 7

  if target == start_days % 7:
    print('Sunday')
  elif target == (start_days + 1) % 7:
    print('Monday')
  elif target == (start_days + 2) % 7:
    print('Tuesday')
  elif target == (start_days + 3) % 7:
    print('Wednesday')
  elif target == (start_days + 4) % 7:
    print('Thursday')
  elif target == (start_days + 5) % 7:
    print('Friday')
  else:
    print('Saturday')
else:
  print('ERROR')