
#read in the boardingpass file
output = open("boardingpass.txt", "r")
seatlist = []

#for each boarding pass separate the row and column 
for aline in output:
    row = aline[:7]
    column = aline.strip()[-3:]

    #to work out the seat
    colmin=0
    colmax=7

    for letter in column:
        if letter == 'R':
            colmin = colmin+((colmax-colmin)//2)+1
        else:
            colmax = colmax-((colmax-colmin)//2)-1

    #to work out the row
    rowmin=0
    rowmax=127

    for letter in row:
        if letter == 'B':
            rowmin = rowmin+((rowmax-rowmin)//2)+1
        else:
            rowmax = rowmax-((rowmax-rowmin)//2)-1

    seatid=(rowmin*8)+colmin

    #add seatid to list
    seatlist.append(seatid)
    
seatlist=sorted(seatlist)

start, end = seatlist[0], seatlist[-1]
print(sorted(set(range(start, end + 1)).difference(seatlist)))





    


