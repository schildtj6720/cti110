# Jasmine Schildt
# 10/23/2024
# P3LAB
# An assignment that tests knowledge of how to display information to users and calculates needed change from an amount of money.

money_amount = float(input('Enter the amount of money as a float: $'))

# Dollars
dollars = int(money_amount) // 1
dol_remainder = (money_amount - dollars) 

# Cents
quarters = (money_amount - dollars) // .25
quarters = int(quarters)

dimes = (money_amount - dollars - quarters) // .10
dimes = int(dimes)

nickels = (money_amount - dollars - quarters - dimes) // .5
nickels = int(nickels)

pennies = (money_amount - dollars - quarters - dimes - nickels) // .01
pennies = int(pennies)

if (money_amount == 0):
    print('No change')

if dollars > 1:
    print(dollars,'Dollars')
if dollars == 1:
    print(dollars,'Dollar')

if quarters > 1:
    print(quarters,'Quarters')
if quarters == 1:
    print(quarters,'Quarter')
    
if dimes > 1:
    print(dimes, 'Dimes')
if dimes == 1:
    print(dimes, 'Dime')
    
if nickels > 1:
    print(nickels, 'Nickels')
if nickels == 1:
    print(nickels, 'Nickel')
    
if pennies > 1:
    print(pennies, 'Pennies')
if pennies == 1:
    print(pennies, 'Penny')
