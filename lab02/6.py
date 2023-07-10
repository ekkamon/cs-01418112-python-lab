count = int(input())
firstChar = str(input())
secondChar = str(input())

print((firstChar + secondChar) * (count // 2) + firstChar * (count % 2))