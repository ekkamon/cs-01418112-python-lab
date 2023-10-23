def is_dupicate_values(data):
  last = data[0]
  
  for val in data:
    if val != last:
      return False
    
  return True

def is_random_sort(data):
  last = data[0]
  status = []
  
  for idx in range(len(data)-1):
    val = data[idx]
    
    if val > data[idx+1]:
      status.append(1)
      
    if val < data[idx+1]:
      status.append(2)
  
  return True if not is_dupicate_values(status) else False

def is_non_increasing(data):
  last = data[0]
  
  for idx in range(len(data)-1):
    val = data[idx]
    
    if val > data[idx+1]:
      return True
    
  return False
    
def check_order(data):
  # check empty data
  if len(data) == 0:
    return 'The list is empty.'
  
  # check same values
  if is_dupicate_values(data):
    return 'The list is in non-increasing and non-decreasing order.'
  
  # check random sort
  if is_random_sort(data):
    return 'The list is in random order.'
  
  # check increasing or decreasing
  return f'The list is in non-{"increasing" if is_non_increasing(data) else "decreasing"} order.'

def main():
  data = []
  
  while True:
    num = int(input('Enter a number (-1 to end): '))
    
    if num == -1:
      break
    
    if num < 0 or num > 100:
      print('Number is out of range.')
      continue
    
    data.append(num)

  print('-----')
  print('Original list:')
  print(data)
  print(check_order(data))
  
main()