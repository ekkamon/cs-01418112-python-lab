width = float(input("Enter width: "))
length = float(input("Enter length: "))
depth = float(input("Enter depth: "))

pool = width * length * depth

print('Time to fill a pool is {:.2f} minutes.'.format((pool * 15) / 60))
