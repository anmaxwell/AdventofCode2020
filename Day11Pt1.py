#read in the floorplan
with open("floorplan.txt") as file:
    output = [x for x in file.read().split()]

#set row number, create seatplan and workout size of floorplan
s = 0
seatplan = []
rowlen = len(output[0])
collen = 0

#add each seat to the seatplan with the seat no and state
for row in output:
    for seat in row:
        seatplan.append([s,seat])
        s +=1
    collen +=1

for seat in seatplan:
    if seat[1] != '.':
        seat[1] = 'A'

print(seatplan, rowlen, collen)
print('=======space===========')
