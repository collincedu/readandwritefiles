import csv
#open
customer_country = open("customers.csv", 'r')

#create object
customer_country = csv.reader(customer_country, delimiter = ',')

#open new csv for writing
outfile = open("customer_country.csv", "w")

#for loop: write records to new file
counter = 0
for record in customer_country:
    outfile.write(record[1] + ',' + record[2] + ',' + record[3] + '\n')
    counter += 1

print(counter)
outfile.close()
    