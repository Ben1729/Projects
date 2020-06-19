cases = int(raw_input())

percentAboveAverage = 0


for case in range(cases):
    data = raw_input().split()
    students = int(data[0])
    total = 0
    totalAboveAverage = 0
    
    for student in range(students):
        total += int(data[student+1])

    average = total / (students)
    

    for student in range(students):
        if int(data[student + 1]) > average:
            totalAboveAverage += 1

    percentAboveAverage = float(totalAboveAverage) / students
    print "{:2.3%}".format(percentAboveAverage)