import StudentsUtil

marks = [85, 78, 92, 88, 76]

total = StudentsUtil.calculate_total(marks)
average = StudentsUtil.calculate_average(marks)
grade = StudentsUtil.calculate_grade(average)

print("Marks :",marks)
print("Total :",total)
print("Average :",average)
print("Grade :",grade)
