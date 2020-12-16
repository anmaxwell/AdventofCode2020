import csv


def dy1pt2():

    #read in file from Elves and convert each value to int
    with open('number.csv', 'r') as csvfile:
        mylist = []
        for row in csv.reader(csvfile, delimiter=';'):
                mylist.append(int(row[0]))

    #take in the first number 
    for ind, i in enumerate(mylist):

        remainder1 = 2020 - i

        #take in the second number and find the remainder
        for inj, j in enumerate(mylist, start=ind+1):
            remainder2 = remainder1 - j

            # see if the remainder is in the file and return the product
            if remainder2 in mylist:
                print(remainder2*i*j)
                return

dy1pt2()