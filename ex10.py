#check a prime number
def prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('It is prime number')
    else:
        print('It is not a prime number')
            
n = int(input())
prime(number = n)