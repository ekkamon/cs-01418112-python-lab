nums = []

while True:
    num = int(input('Enter a number (0 to end): '))
    if num == 0:
        break
    
    if num < 1 or num > 999:
        print('Number is out of range.')
        continue
    
    nums.append(num)
    
print('Original list:')
print(nums)
print('Accumulative Sum:')

total = 0

for val in nums:
    total += val
    print(total)
