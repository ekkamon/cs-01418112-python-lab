def count_char(words):
  data = {char.lower():0 for char in words if char.isalpha()}
  
  for char in words:
    char = char.lower()
    
    if char in data:
      data[char] += 1
      
  
  return data

