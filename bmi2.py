#calculating the body mass index by taking height and weight as input 
height = float(input())
weight = int(input())

bmi = weight / (height * height)
if bmi < 18.5:
  print(f'your BMI is {bmi} you are underweight')
elif bmi < 25:
  print(f'your BMI is {bmi} you are idealweight')
elif bmi < 30:
  print(f'your BMI is {bmi} you are overweight')
elif bmi < 35:
  print(f'your BMI is {bmi} you are obese')
else:
  print(f'your BMI is {bmi} you are critical')
