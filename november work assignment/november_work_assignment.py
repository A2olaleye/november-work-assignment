def calculate_average_and_grade(test_scores, c_barrier, b_barrier, a_barrier):
    average = sum(test_scores) / len(test_scores)
    total_marks = sum(test_scores)
    
    if average >= a_barrier:
        grade = 'A'
    elif average >= b_barrier:
        grade = 'B'
    elif average >= c_barrier:
        grade = 'C'
    else:
        grade = 'Below C'
    
    return average, total_marks, grade


def english_grades(test1, test2):
    test_scores = [test1, test2]
    c_barrier, b_barrier, a_barrier = 64/120, 84/120, 104/120
    return calculate_average_and_grade(test_scores, c_barrier, b_barrier, a_barrier)


def maths_grades(test1, test2, test3):
    test_scores = [test1, test2, test3]
    c_barrier, b_barrier, a_barrier = 56/100, 64/100, 78/100
    return calculate_average_and_grade(test_scores, c_barrier, b_barrier, a_barrier)


def science_grades(test1, test2, test3):
    test_scores = [test1, test2, test3]
    c_barrier, b_barrier, a_barrier = 96/150, 113/150, 128/150
    return calculate_average_and_grade(test_scores, c_barrier, b_barrier, a_barrier)

english_result = english_grades(50, 70)
maths_result = maths_grades(45, 60, 75)
science_result = science_grades(90, 110, 120)

print(f"English: Average={english_result[0]:.2f}, Total Marks={english_result[1]}/240, Grade={english_result[2]}")
print(f"Maths: Average={maths_result[0]:.2f}, Total Marks={maths_result[1]}/300, Grade={maths_result[2]}")
print(f"Science: Average={science_result[0]:.2f}, Total Marks={science_result[1]}/360, Grade={science_result[2]}")
