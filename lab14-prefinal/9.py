def get_unique_data(data):
  unique = []
  
  for val in data:
    if val not in unique:
      unique.append(val)
      
  return unique

def find_majority_element(arr, n):
  for val in get_unique_data(arr):
    if arr.count(val) >= n:
      return val
    
  return 0

def main():
  count = int(input())
  data = [str(input()) for _ in range(count)]
  
  print(find_majority_element(data, (count // 2) + 1))

main()