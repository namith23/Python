print(70 + float("100.5"))
print(str(70)+str(100))
print(70 + int('100'))

#prog to do add one two digit number ex-32(3+2=5)
#
output = input("Enter two digits of number:")
#reading the 1st num
first_digit = int(output[0])
#reading the 2nd num
second_digit = int(output[1])
#adding the 1st and 2nd num
sum = first_digit + second_digit
#then printing the output 
print(f'The sum is :{sum}')