# Jasmine Schildt
# 11/26/2024
# P5HW
# An assignment that challenges the user with subtraction and addition problems.

def intro():
    print('Welcome to Math Quiz')
    print()
    print()
    print('MAIN MENU')
    print('---------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()
    
def adding_random_nums():
    import random
    
    number_one = random.randint(1,100)
    number_two = random.randint(1,100)
    true_answer = number_one + number_two
    int(true_answer)
    
    print()
    print(' ', number_one)
    print('+', number_two)
    print()
    
    adding_answer = int(input('Enter answer: '))
    guess_num = 0
    
    print()
    
    while adding_answer != true_answer:
        if adding_answer < true_answer:
            print('Answer is too low.')
            print()
            
            adding_answer = int(input('Try again: '))
            guess_num += 1
        elif adding_answer > true_answer:
            print('Answer is too high.')
            print()
            
            adding_answer = int(input('Try again: '))
            guess_num += 1
    
    if adding_answer == true_answer:
        print('Congratulations! You are correct!')
        print(f'Number of guesses: {guess_num}')

def subtracting_random_nums():
    import random
    
    number_one = random.randint(1,100)
    number_two = random.randint(1,100)
    true_answer = number_one - number_two
    int(true_answer)
    
    print()
    print(' ', number_one)
    print('-', number_two)
    print()
    
    adding_answer = int(input('Enter answer: '))
    guess_num = 0
    
    print()
    
    while adding_answer != true_answer:
        if adding_answer < true_answer:
            print('Answer is too low.')
            print()            
            
            adding_answer = int(input('Try again: '))
            guess_num += 1
        elif adding_answer > true_answer:
            print('Answer is too low.')
            print()                      
            
            adding_answer = int(input('Try again: '))
            guess_num += 1
    
    if adding_answer == true_answer:
        print('Congratulations! You are correct!')
        print(f'Number of guesses: {guess_num}')

intro()

menu_option = input('Please choose one of the menu options: ')

while menu_option == '1' or '2' or '3':
    if menu_option == '1':
        adding_random_nums()
    
        print()
    
        intro()
    elif menu_option == '2':
        subtracting_random_nums()
    
        print()
        
        
        intro()
    elif menu_option == '3':
        print('Thank you for playing...')
        print('Bye!!')
        exit()
    else:
        print()
        print('ERROR: Please enter 1, 2, or 3.')
        print()
    
        intro()
        menu_option = input('Please choose one of the menu options: ')
