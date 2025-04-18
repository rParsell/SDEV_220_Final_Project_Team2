import csv

fileName = "employees.csv"

fields = ['Employee ID','First Name','Last Name','Shift','Hours','Department','Sunday Available',
          'Monday Available','Tuesday Available','Wednesday Available', 'Thursday Available',
           'Friday Available', 'Saturday Available' ]



rows = [  ['001','fName1','lName1','1', '40', 'Customer Service', 'True','False','True','True','True','False','True'],
          ['002','fName2','lName2','1', '40', 'Customer Service', 'True','True','True','True','False','True','True'],
          ['003','fName3','lName3','1', '40', 'Customer Service', 'True','True','False','True','True','True','True'],
          ['004','fName4','lName4','1', '40', 'Customer Service', 'True','True','True','True','True','True','False'],
          ['005','fName5','lName5','1', '40', 'Customer Service', 'False','True','True','True','True','True','True'],
          ['006','fName6','lName6','2', '40', 'Customer Service', 'True','True','True','True','False','True','True'],
          ['007','fName7','lName7','2', '40', 'Customer Service', 'False','True','True','True','True','True','True'],
          ['008','fName8','lName8','2', '40', 'Customer Service', 'True','False','True','True','True','True','True'],
          ['009','fName9','lName9','2', '40', 'Customer Service', 'True','True','True','False','True','True','True'],
          ['010','fName10','lName10','2', '40', 'Customer Service', 'True','True','False','True','True','True','True'],
          ['011','fName11','lName11','1', '40', 'Grocery', 'True','True','True','True','True','False','True'],
          ['012','fName12','lName12','1', '40', 'Grocery', 'True','True','False','True','True','True','True'],
          ['013','fName13','lName13','1', '40', 'Grocery', 'True','True','True','True','True','True','False'],
          ['014','fName14','lName14','1', '40', 'Grocery', 'False','True','True','True','True','True','True'],
          ['015','fName15','lName15','2', '40', 'Grocery', 'True','True','True','True','True','True','True'],
          ['016','fName16','lName16','2', '40', 'Grocery', 'True','True','True','False','True','True','True'],
          ['017','fName17','lName17','2', '40', 'Grocery', 'True','False','True','True','True','True','True'],
          ['018','fName18','lName18','3', '40', 'Grocery', 'True','False','True','True','True','True','True'],
          ['019','fName19','lName19','3', '40', 'Grocery', 'True','True','True','True','False','True','True'],
          ['020','fName20','lName20','3', '40', 'Grocery', 'False','True','True','True','True','True','True'],
        ]

with open(fileName, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)

# reading csv file
with open(fileName, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    # remove hashes below when you want to update data
   # for row in csvreader:
   #     rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nPrinting Rows:\n')
for row in rows:
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')
