days_name = str(input())
target_days = int(input())

is_error = False

days_value = 0

if days_name == 'Sunday':
  days_value = 1
elif days_name == 'Monday':
  days_value = 2
elif days_name == 'Tuesday':
  days_value = 3
elif days_name == 'Wednesday':
  days_value = 4
elif days_name == 'Thursday':
  days_value = 5
elif days_name == 'Friday':
  days_value = 6
elif days_name == 'Saturday':
  days_value = 7
else:
  is_error = True

if target_days <= 0 or target_days > 31:
  is_error = True

if not is_error:
  target = ((target_days + (days_value - 1)) % 7)

  if target == 1:
    print('Sunday')
  elif target == 2:
    print('Monday')
  elif target == 3:
    print('Tuesday')
  elif target == 4:
    print('Wednesday')
  elif target == 5:
    print('Thursday')
  elif target == 6:
    print('Friday')
  else:
    print('Saturday')
else:
  print('ERROR')