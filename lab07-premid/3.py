days = int(input())
hours = int(input())
minutes = int(input())

today_is = ''
greeting = ''

if days == 1:
  today_is = 'sunday'
elif days == 2:
  today_is = 'monday'
elif days == 3:
  today_is = 'tuesday'
elif days == 4:
  today_is = 'wednesday'
elif days == 5:
  today_is = 'thursday'
elif days == 6:
  today_is = 'friday'
elif days == 7:
  today_is = 'saturday'

minutes += hours * 60

if minutes > 4 * 60 and minutes <= 12 * 60:
  greeting = 'morning'
elif minutes > 12 * 60 and minutes <= 18 * 60:
  greeting = 'afternoon'
elif minutes > 18 * 60 and minutes <= 22 * 60:
  greeting = 'evening'
else:
  greeting = 'night'

print(f'good-{greeting}-{today_is}.png')