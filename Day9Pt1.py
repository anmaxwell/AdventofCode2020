#read in the list of numbers
output = open("xmaslist.txt", "r")

#set the preamble number 
preamble = 25

#create the blank list 
xmaslist = []

#add each number to the list for comparison
for item in output:
    xmaslist.append(int(item.strip()))

#create the list to fin the final result
dupelist = xmaslist[preamble:]

#check each value in the list
for i in range(len(xmaslist)-preamble):
    partlist = xmaslist[i:i+preamble]
    
    value = xmaslist[i+preamble]

    #remove each value that has a sum from the list
    for check in partlist:
        result = value-check
        if result in partlist and result != check:
            dupelist.remove(value)
            break


print('answer', dupelist)