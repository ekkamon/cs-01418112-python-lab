weight = float(input('Weight (kg): '))
height = float(input('Height (m): '))

bmi = weight / (height ** 2)

print('BMI is {:.1f}'.format(bmi))

if bmi >= 30:
    print('Obesity')
elif bmi >= 25:
    print('Overweight')
elif bmi >= 18.5:
    print('Normal weight')
else:
    print('Underweight')