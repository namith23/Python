#tip calculator

print("Welcome to the tip calculator")
tot_bill = float(input('What was the total bill:\n'))
tip_percentage = int(input('What percentage tip would You like to give:\n'))
tip_amt = tip_percentage / 100 * tot_bill
total_amt = tip_amt + tot_bill
equal_pay = int(input('How many people to split the bill?\n'))
pay  = round(total_amt / equal_pay,2)#round is used to round off the num to the required decimal places  round(variable_name,no of decimal places to be round off)
print('Each person should pay:',pay)
