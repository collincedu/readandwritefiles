import csv
import locale 
locale.setlocale(locale.LC_ALL, '')


infile = open("EmployeePay.csv", 'r')

reader = csv.reader(infile, delimiter = ',')

#print new headers and skip old header column
print('ID', 'EmpFName', 'EmpLName', 'Bonus', 'TotalPay', sep=',')
next(reader)

for row in reader:
    emp_id = row[0]
    lname = row[1]
    fname = row[2]
    salary = float(row[3])
    bonus = float(row[4])
    cash_bonus = salary * bonus
    cash_total_pay = salary *(1 + bonus)

    print(emp_id, fname, lname, locale.currency(cash_bonus, grouping=True), locale.currency(cash_total_pay, grouping=True), sep=',')

    input()


