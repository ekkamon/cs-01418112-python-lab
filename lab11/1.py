nums = int(input())

def get_max_space():
    count = 1
    for i in range(nums): count += 2
    return count - 2

space = 1
max_space = get_max_space()

for i in range(nums):
    print("|" + f'{("*" * space):^{max_space}}' +"|")
    space += 2