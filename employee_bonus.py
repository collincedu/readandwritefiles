import csv

infile = open("EmployeePay.csv", 'r')

employee_bonus = csv.reader(, delimiter = ',')

for record in infile:
    print(record)

#pause
input()