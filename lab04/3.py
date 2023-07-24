tv = int(input('How many TVs? '))
dvd = int(input('How many DVD players? '))
audio = int(input('How many Audio Systems? '))

if tv < 0:
    tv = 0
    
if dvd < 0:
    dvd = 0
    
if audio < 0:
    audio = 0
    
tv *= 6000
dvd *= 1500
audio *= 3000

totalPrice = tv + dvd + audio

print(f'Total price is {totalPrice:.2f} baht.')

if totalPrice >= 24_000:
    discount = totalPrice * (20/100)
    totalPrice -= discount
    
    print(f'You\'ve got a discount of {discount:.2f} baht.')
    
print(f'Your payment is {totalPrice:.2f} baht. Thank you!')