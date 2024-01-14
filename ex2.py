print('Welcome')
name1 = input('Enter name1:')
name2 = input('Enter name2:')
full_name = name1 + name2
lowername = full_name.lower()
t = lowername.count("t")
r = lowername.count("r")
u = lowername.count("u")
e = lowername.count("e")
first_digit = t + r + u + e
l = lowername.count("l")
o = lowername.count("o")
v = lowername.count("v")
e = lowername.count("e")
second_digit = l + o + v + e
total = int(str(first_digit) + str(second_digit))

if (total < 10) or (total > 90):
    print(f'your score is {total},you go together like coke and mentos ')
elif (total >= 40) & (total <=50):
    print(f'your score is {total},you are alright together')
else:
    print(f'your score is {total}')