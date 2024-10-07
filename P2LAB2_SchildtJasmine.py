# Jasmine Schildt
# 10/6/2024
# P2LAB2
# An assignment that utilizes dictionary, input, and output knowledge.

car_types = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

keys = car_types.keys()

print(keys)
print(' ')

vehicle = input('Enter a vehicle to see its mpg: ')
print(' ')

print('The',vehicle, 'gets', car_types[vehicle], 'mpg.')
mpg = int(car_types[vehicle])
print(' ')

print('How many miles will you drive the', vehicle + '?', end=' ')
miles = int(input())
print(' ')

print(f'{(1 / mpg)*50:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.')
