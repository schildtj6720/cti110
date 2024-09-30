# Jasmine Schildt
# 9/29/2024
# P1HW2
# An assignment used to practice and testing code using IDLE.

# Recieve budget input.
# Recieve destination input.
# Recieve gas input.
# Recieve accomodation/hotel input.
# Recieve food input.
# Calculate remaining balance.
# Display Travel Expense data.
# Display Remaining Balance

print('This program calculates and displays travel expenses\n')
print('Enter budget:', end=' ')
budget = int(input())
print('')
print('Enter your travel destination', end=' ')
destination = input()
print('')
print('How much do you think you will spend on gas?', end=' ')
gas = int(input())
print('')
print('Approximately, how much will you need for accomodation/hotel?', end=' ')
accomodation = int(input())
print('')
print('Last, how much do you need for food?', end=' ')
food = int(input())
print('')
rem_balance = budget - gas - accomodation - food

print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget:', budget, '\n')
print('Fuel:', gas)
print('Accomodation:', accomodation)
print('Food:', food, '\n')

print('Remaining Balance:', rem_balance)
