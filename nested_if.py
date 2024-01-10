print('Welcome to the Rollercoster')
height = int(input('enter your height: '))

if height >= 120:
    print('you can ride')
    age = int(input('Enter you age:'))
    
    if age >= 18:
        print('your fair is $12')
    elif age < 12:
        print('your fair is $5')
    else:
        print('your fair is $7')

    
else:
    print('you cannot ride')