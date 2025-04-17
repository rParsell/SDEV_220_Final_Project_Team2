import csv

fileName = "employees.csv"

fields = ['Employee ID','First Name','Last Name','Shift','Hours','Department','Sunday Available',
          'Monday Available','Tuesday Available','Wednesday Available', 'Thursday Available',
           'Friday Available', 'Saturday Available' ]
rows = [  ['001','fName1','lName1','1', '40', 'Customer Service', 'True','True','True','True','True','True','True'],
          ['002','fName1','lName1','1', '40', 'Customer Service', 'True','True','True','True','True','True','True'],
          ['003','fName1','lName1','1', '40', 'Customer Service', 'True','True','True','True','True','True','True'],
          ['004','fName1','lName1','1', '40', 'Customer Service', 'True','True','True','True','True','True','True'],
          ['005','fName1','lName1','1', '40', 'Customer Service', 'False','True','True','True','True','True','True'],
          ['006','fName1','lName1','2', '40', 'Customer Service', 'True','True','True','True','True','True','True'],
          ['007','fName1','lName1','2', '40', 'Customer Service', 'False','True','True','True','True','True','True'],
          ['008','fName1','lName1','2', '40', 'Customer Service', 'True','True','True','True','True','True','True'],
          ['009','fName1','lName1','2', '40', 'Customer Service', 'True','True','True','False','True','True','True'],
          ['010','fName1','lName1','2', '40', 'Customer Service', 'True','True','True','True','True','True','True'],
          ['011','fName1','lName1','1', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['012','fName1','lName1','1', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['013','fName1','lName1','1', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['014','fName1','lName1','1', '40', 'Grocery', 'False','True','True','True','True','True','True'],
          ['015','fName1','lName1','2', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['016','fName1','lName1','2', '40', 'Grocery', 'True','True','True','False','True','True','True'],
          ['017','fName1','lName1','2', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['018','fName1','lName1','3', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['019','fName1','lName1','3', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['020','fName1','lName1','3', '40', 'Grocery', 'False','True','True','True','True','True','True'],
        ]

# reading csv file
with open(fileName, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')