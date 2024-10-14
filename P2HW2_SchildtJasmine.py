# Jasmine Schildt
# 10/14/2024
# P2HW2
# An assignment that analyzes grades and helps student understanding of lists.

# Input grades for module 1, 2, 3, 4, 5, and 6
# Perform float conversion to turn the list "grade_collection" into floating point numbers
# Find the minimum, maximum, sum, and average of grade_collection using sequence-type operations
# Display results

grade1 = input('Enter grade for module 1: ')
grade2 = input('Enter grade for module 2: ')
grade3 = input('Enter grade for module 3: ')
grade4 = input('Enter grade for module 4: ')
grade5 = input('Enter grade for module 5: ')
grade6 = input('Enter grade for module 6: ')

grade_collection = [float(grade1), float(grade2), float(grade3), float(grade4), float(grade5), float(grade5)]

print(' ')

print('------------Results------------')

lowest_grade = min(grade_collection)
highest_grade = max(grade_collection)
grade_sum = sum(grade_collection)
grade_average = max(grade_collection) / 6

print(f'Lowest grade:       {lowest_grade:.1f}')
print(f'Highest grade:      {highest_grade:.1f}')
print(f'Sum of grades:      {highest_grade:.1f}')
print(f'Average:            {highest_grade:.2f}')

print('--------------------------------------')
