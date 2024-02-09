#Calculator for online pizza delivery based on the size of pizza, extra pepperoni and extra cheese
print("Thank you for choosing Python Pizza Deliveries!")
size = input('What size pizza do you want? S, M, or L\n') # What size pizza do you want? S, M, or L
add_pepperoni = input('Do you want pepperoni? Y or N\n') # Do you want pepperoni? Y or N
extra_cheese = input('Do you want extra cheese? Y or N\n') # Do you want extra cheese? Y or N
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1

print(f"Your final bill is: ${bill}.")
