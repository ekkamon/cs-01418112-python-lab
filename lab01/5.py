blockLength = int(input("Enter block length: "))
blockWidth = int(input("Enter block width: "))
houseLength = int(input("Enter house length: "))
houseWidth = int(input("Enter house width: "))

totalHouse = houseLength * houseWidth
totalBlock = blockLength * blockWidth

print('Mowing cost is', (totalBlock - totalHouse) * 35, 'baht.')