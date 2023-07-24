year = int(input('Enter year: '))

if year <= 0:
  print('Invalid year.')
else:
  isLeapYear = False

  if year % 4 == 0 and year % 100 > 0:
    isLeapYear = True
  elif year % 400 == 0:
    isLeapYear = True

  print(year, 'is' if isLeapYear else 'is not', 'a leap year.')
