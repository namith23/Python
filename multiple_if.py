height = int(input('Enter your height:'))
age = int(input('Enter your age:'))
cost = 0

if height > 120:
    print('Can ride')
    if age > 18:
        bill = 12
        print('your fair is $12')
    if age > 12:
        bill = 7
        print('your fair is $7')
    if age < 12:
        bill = 5
        print('your fair is $5')
        
    want_photo = input('Do u want to take a photo? Y or N')
    if want_photo == "Y":
        bill += 3
else:
    print('Cant ride')

print('Your fair is ',bill)