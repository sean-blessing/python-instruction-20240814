# declare the dictionary
scores_by_student = {}

with open("./files/testscores.dat") as scores_in:
    # loop through file and create dictionary entries
    for line in scores_in:
        name, score = line.split(":")
        # print(f'name: {name}, score: {score}')
        # convert score to an int
        score = int(score)
        # add entry to the dictionary
        scores_by_student[name] = score

# print student name, score, and letter grade
for student, score in scores_by_student.items():
    letter_grade = 'F'
    if score > 94:
        letter_grade = 'A'
    elif score > 88:
        letter_grade = 'B'
    elif score > 82:
        letter_grade = 'C'
    elif score > 74:
        letter_grade = 'D'
    print(f'{student:20s} {score} {letter_grade}')

# compute the average
# sum of all scores, compute the average: sum / # of scores
sum_scores = sum(scores_by_student.values())
average = sum_scores / len(scores_by_student)
print(f'\n Average score: {average:.2f}')
