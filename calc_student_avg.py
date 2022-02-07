import csv

student_avg = open("Student_Scores.csv", 'r')

reader = csv.reader(student_avg, delimiter = ',')

#create new csv for writing
outfile = open("student_avg.csv", "w")

#for loop
for row in reader:
    name = row[0]
    grade1 = float(row[1])
    grade2 = float(row[2])
    grade3 = float(row[3])
    avg_grade = "{:.2f}".format(round(grade1 + grade2 + grade3) / 3)

    outfile.write(name)
    outfile.write(' ')
    outfile.write(avg_grade)
    outfile.write('\n')

#close
outfile.close()



