import csv

#read in file from Elves and convert each value to int
with open('number.csv', 'r') as csvfile:
    mylist = []
    for row in csv.reader(csvfile, delimiter=';'):
            mylist.append(int(row[0]))

#take each number to check the remainder
for i in mylist:
    remainder = 2020 - i

    # see if the remainder is in the file and return the product
    if remainder in mylist:
        print(remainder*i)
        break
        
