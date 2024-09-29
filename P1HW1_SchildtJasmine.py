# Jasmine Schildt
# 9/29/2024
# P1HW1
# An assignment used to practice collecting and processing information and displaying the results of it.

print('-----Calculating Exponents-----\n\n\nEnter an integer as the base value:', end=' ')
base_value = int(input())
print('Enter an integer as the exponent:', end=' ')
exponent = int(input())
print('\n')
print(base_value, 'raised to the power of', exponent, 'is', (pow(base_value,exponent)), '!!')
print('\n')

print('-----Addition and Subtraction-----\n\n\nEnter a starting integer:', end=' ')
starting_int = int(input())
print('Enter an integer to add:', end=' ')
add_int = int(input())
print('Enter an integer to subtract:', end=' ')
subtract_int = int(input())
result = starting_int + add_int - subtract_int
print('\n')

print(starting_int, '+', add_int, '-', subtract_int, 'is equal to', result)
