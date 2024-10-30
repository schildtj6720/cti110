# Jasmine Schildt
# 10/30/2024
# P3HW2
# An assignment that assesses student understanding of decision structures.

# user input is obtained
employee_name = input('Enter Employee\'s name: ')
hours_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input('Enter employee\'s pay rate: '))

# employee gross pay and overtime hours are calculated
gross_pay = hours_worked * pay_rate
overtime = (hours_worked - 40)

# employee overtime evaluation
if (hours_worked > 40):
    overtime_pay = (overtime * pay_rate)
else:
    overtime_pay = 0
    
# regular hours and pay are calculated
reg_hours = (hours_worked - overtime)
reghour_pay = ((hours_worked - 40) * pay_rate)

print('---------------------------')

# employee pay information is displayed
print('Employee name:', employee_name)
print(' ')
print('Hours worked     Pay Rate     Overtime     Overtime Pay    Reghour Pay     Gross Pay')
print(f'{hours_worked:<17.2f}{pay_rate:<13.2f}{overtime:<13.2f}{overtime_pay:<16.2f}{reghour_pay:<16.2f}{gross_pay:<15.2f}')