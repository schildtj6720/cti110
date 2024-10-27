# Jasmine Schildt
# 10/23/2024
# P3HW1
# An assignment that builds on P2HW2's lists.

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [float(mod_1), float(mod_2), float(mod_3), float(mod_4), float(mod_5), float(mod_6)]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_ = sum(grades)
avg =  max(grades) / 6

print(' ')

print('------------Results------------')

# Print grade results

print(f'Lowest grade:       {low:.1f}')
print(f'Highest grade:      {high:.1f}')
print(f'Sum of grades:      {sum_:.1f}')
print(f'Average:            {avg:.2f}')

print('--------------------------------------')

# determine letter grade for average

if avg >= 90.00:
    print('Your grade is: A')
    
if avg >= 80.00 and avg <= 89.00:
    print('Your grade is: B')
    
if avg >= 70.00 and avg <= 79.00:
    print('Your grade is: C')
    
if avg >= 60.00 and avg <= 69.00:
    print('Your grade is: D')
    
if avg >= 00.00 and avg <= 59:
    print('Your grade is: F')
