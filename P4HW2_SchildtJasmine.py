# Jasmine Schildt
# 11/13/2024
# P4HW2
# An assignment that assess student ability to edit and enhance exiting programs.

# lists are made to store employee info
# employee name is asked
# employee info is obtained
# employee gross pay and overtime hours are calculated
# employee overtime evaluation
# regular hours and pay are calculated
# employee pay information is displayed
# results are displayed

# lists are made to store employee info

total_employees = 0
total_overtime = []
total_reghourpay = []
total_grosspay = []

# employee name is asked
employee_name = ''

while employee_name != 'Done':
    employee_name = input('Enter Employee\'s name or "Done" to terminate: ')
    
    if employee_name == 'Done':
        print('')
        break
    
    total_employees += 1
    
    # employee info is obtained
    hours_worked = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    # employee gross pay and overtime hours are calculated
    gross_pay = hours_worked * pay_rate
    total_grosspay.append(gross_pay)
    overtime = (hours_worked - 40)
    total_overtime.append(overtime)
    
    # employee overtime evaluation
    if (hours_worked > 40):
        overtime_pay = (overtime * pay_rate)
    else:
        overtime_pay = 0
        
    # regular hours and pay are calculated
    reg_hours = (hours_worked - overtime)
    reghour_pay = ((hours_worked - 40) * pay_rate)
    total_reghourpay.append(reghour_pay)
    
    print('---------------------------')
    
    # employee pay information is displayed
    print('Employee name:', employee_name)
    print(' ')
    print('Hours worked     Pay Rate     Overtime     Overtime Pay    Reghour Pay     Gross Pay')
    print(f'{hours_worked:<17.2f}{pay_rate:<13.2f}{overtime:<13.2f}{overtime_pay:<16.2f}{reghour_pay:<16.2f}{gross_pay:<15.2f}')
    
    print(' ')
    

# results are displayed
print(f'Total number of employees entered: {total_employees}')
print(f'Total amount paid for overtime: {sum(total_overtime)}')
print(f'Total amount paid for regular hours: {sum(total_reghourpay)}')
print(f'Total amount paid in gross: {sum(total_grosspay)}')
