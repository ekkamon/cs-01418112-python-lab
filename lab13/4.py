def get_date_value():
  data = str(input()).split('-')

  if len(data) < 2:
    return [0, 0]
  
  return [int(val) if val != '' else 0 for val in data]

def get_max_day_by_month(month):  
  if month == 2:
    return 28
  
  return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30

def print_verbose_error(errors):
  status = ['Wrong Month', 'Wrong Day']
  is_prints = []
  
  errors.sort()
  
  for val in errors:
    if val in is_prints:
      continue
    
    is_prints.append(val)
    print(status[val])

def is_date_error(sunday, date):
  errors = []
  
  if sunday < 1:
    errors.append(1)
  
  for day, month in date:
    if month < 1 or month > 12:
      errors.append(0)
      
    if day < 1 or day > 31:
      errors.append(1)
    
    if (month >= 1 and month <= 12) and day > get_max_day_by_month(month):
      errors.append(1)
      
  if len(errors) > 0:
    print_verbose_error(errors)
    return True
  
  return False

def swap_date(start_date, end_date):
  [start_day, start_month], [end_day, end_month] = start_date, end_date
  
  if (start_day > end_day and start_month >= end_month) or start_month > end_month:
    start_date, end_date = end_date, start_date
    
  return start_date, end_date

def get_last_sunday(sunday, max_day):  
  for day in range(max_day, 1, -1):
    if day % 7 == sunday % 7:
      return day
    
def get_first_sunday(last_sunday, max_day):
  return (last_sunday + 7) % max_day
    
def get_first_sunday_all_months(sunday):
  data = [sunday]
  months = [month for month in range(2, 13)]
  
  last_sunday = get_last_sunday(sunday, 31)
  first_sunday = get_first_sunday(last_sunday, 31)
  
  for month in months:
    data.append(first_sunday)
    
    max_day = get_max_day_by_month(month)
    last_sunday = get_last_sunday(first_sunday, max_day)
    first_sunday = get_first_sunday(last_sunday, max_day)
    
  return data
    
def get_sunday_count_of_month(sunday, start, end):
  return len([day for day in range(start, end + 1) if day % 7 == sunday % 7])


def get_sunday_count_between_date(sunday, start_date, end_date):
  [start_day, start_month], [end_day, end_month] = start_date, end_date
  
  total = 0
  months = [month for month in range(start_month, end_month + 1)]  
  start_sunday_of_months = get_first_sunday_all_months(sunday)
  
  for idx in range(len(months)):
      month = months[idx]
      start = start_day if idx == 0 else 1
      end = end_day if idx == (len(months) - 1) else get_max_day_by_month(month)
      total += get_sunday_count_of_month(start_sunday_of_months[month-1], start, end)
      
  return total

def main():
  start_date = get_date_value()
  end_date = get_date_value()
  sunday = int(input())
  
  # swap date
  start_date, end_date = swap_date(start_date, end_date)
  
  # check error
  if is_date_error(sunday, [start_date, end_date]):
    return

  print(get_sunday_count_between_date(sunday, start_date, end_date))

main()