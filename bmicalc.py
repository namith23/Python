height = input()
weight = input()

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float**2
print(bmi)#return output in floating num
bmi_as_int = int(bmi)#to convert float into int
print(bmi_as_int)#return output in integer