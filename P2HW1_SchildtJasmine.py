# Jasmine Schildt
# 10/13/2024
# P2HW1
# An assignment that builds on the P1HW2 assignment.

print('This program calculates and displays travel expenses\n')
print('Enter budget:', end=' ')
budget = int(input())
print('')
print('Enter your travel destination:', end=' ')
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
print(f'Location:          {destination}')
print(f'Initial Budget:    ${budget:.2f}')
print(f'Fuel:              ${gas:.2f}')
print(f'Accomodation:      ${accomodation:.2f}')
print(f'Food:              ${food:.2f}')
print('---------------------------------------', '\n')

print(f'Remaining Balance: ${rem_balance:.2f}')

