distance = int(input())
fuel = int(input())

# 15 km / 1 lit

needFuel = distance / 15

print(int(needFuel // (fuel * 50/100) + 1))
print(int(needFuel // (fuel * 90/100) + 1))