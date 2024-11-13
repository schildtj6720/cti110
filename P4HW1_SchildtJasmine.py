# Jasmine Schildt
# 11/13/2024
# P4HW1
# An assignment that evaluates scores and assess student ability to edit and enhance exiting programs.

# Ask user how many scores they want to enter + gather scores and create list
# Gather scores
# Make modified list + calculate score details
# Determine grade
# Display results

# Ask user how many scores they want to enter + gather scores and list
num_of_scores = int(input('How many scores do you want to enter?: '))
score_num = 0

score_list = []

print('')

while num_of_scores > 0:
    score_num += 1
    num_of_scores -= 1
    scores = int(input(f'Enter score #{score_num}: '))
    if (scores > 0) and (scores < 100):
        score_list.append(scores)
    else:
        while (scores > 0) and (scores < 100) == False:
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            scores = int(input(f'Enter score #{score_num} again: '))
        score_list.append(scores)

# Make modified list + calculate score details
low_score = min(score_list)

modified_list = []
for item in score_list:
    modified_list.append(float(item))
modified_list.remove(min(modified_list))

ml_sum = sum(modified_list)
ml_len = len(modified_list)
scores_avg = ml_sum / ml_len

# Determine grade
if scores_avg >= 90.00:
    grade = 'A'
elif scores_avg >= 80.00 and scores_avg <= 89.00:
    grade = 'B'
elif scores_avg >= 70.00 and scores_avg <= 79.00:
    grade = 'C'
elif scores_avg >= 60.00 and scores_avg <= 69.00:
    grade = 'D'
elif scores_avg >= 00.00 and scores_avg <= 59:
    grade = 'F'

# Display results
print(' ')

print('------------Results------------')
print(f'Lowest Score  : {float(low_score)}')
print(f'Modified List : {modified_list}')
print(f'Scores Average: {float(scores_avg)}')
print(f'Grade         : {grade}')
print('--------------------------------------')
