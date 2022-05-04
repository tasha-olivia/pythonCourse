student_scores = input("Enter a list of student scores: ").split( )
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# gives the max and min items in a list 
max(student_scores)
min(student_scores)

# manual max
highest_score = 0
for score in student_scores:
    if score >= highest_score:
        highest_score = score
print("The highest score is {highest_score}")