import csv

with open('number.csv', 'r') as csvfile:
    mylist = []
    for row in csv.reader(csvfile, delimiter=';'):
            mylist.append(int(row[0]))

for i in mylist:
    remainder = 2020 - i

    if remainder in mylist:
        print(remainder*i)
        break
        
