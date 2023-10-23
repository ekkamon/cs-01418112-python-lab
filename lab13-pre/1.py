#section 1

ls = []

while True:
    data = str(input())
    
    if data == '':
        break
    
    ls.append(data)
    
#section 2
def create_factors_3_7(n):
   data = []
   num = 1
   
   while len(data) < n:
      if num % 3 == 0 or num % 7 == 0:
         data.append(num)
         
      num += 1
      
   return data