print("="*50)
print("Question 1: Student Grades List")
print("="*50)

grades = [85, 92, 78, 95, 88]

grades.append(90)

grades.sort()

print("Sorted grades:", grades)
print("Hightest grade:", grades[-1])
print("Lowest grad:", grades[0])
print("Total number of grades:", len(grades))