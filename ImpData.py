import csv

def impData(file):
    rows = []
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for col in row:
                rows.append(col)
    return(rows)

print(impData('fake_employee_data.csv'))