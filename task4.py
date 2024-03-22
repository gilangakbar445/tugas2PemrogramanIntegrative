grades = []

while True:
    grade = input("Enter a grade (-1 to end): ")
    if grade == '-1':
        break
    else:
        grades.append(int(grade))

averageGrade = int(sum(grades) / len(grades))

print("Average Grade:", averageGrade)

for grade in grades:
    print(grade)    