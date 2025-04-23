import csv

with open('fake_employee_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for col in row:
            print("%10s" % col, end=" "),
        print('\n')