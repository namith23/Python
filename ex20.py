#bmi using valueError
height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight/height ** 2

if height > 3:
    raise ValueError("The height must not be more than 3")

print(bmi)