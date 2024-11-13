# Jasmine Schildt
# 11/13/2024
# P4LAB2
# An assignment that tests student's knowledge of how to write code that displays information to users using loops.

# define run_again value
# ask user for integer and display calculated results
# correct user after negative number is input
# notify user that program is ending after 'no' is input 

# define run_again value
run_again = 'yes'

# ask user for integer and display calculated results
while run_again != 'no':
    user_num = int(input('Enter an integer: '))
    
    if user_num >= 0:
        for item in range(1,12+1):
            print(f'{user_num} * {item} = {user_num * item}')
    else:
        # correct user after negative number is input
        print('This program does not handle negative values.')
    
    run_again = input('Would you like to run the program again? ')

# notify user that program is ending after 'no' is input  
print('Program is ending.')
