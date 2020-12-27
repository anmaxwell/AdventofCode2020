#read in the list of numbers
output = open("xmaslist.txt", "r")

#set the preamble number 
preamble = 25

#create the blank list of numbers and results
xmaslist = []
answerlist = []

#add each number to the list for comparison
for item in output:
    xmaslist.append(int(item.strip()))

#check each value in the list
for i in range(len(xmaslist)-preamble):
    partlist = xmaslist[i:i+preamble]
    
    value = xmaslist[i+preamble]

    #add each value that has a sum to a new list
    for check in partlist:
        result = value-check
        if result in partlist and result != check:
            answerlist.append(value)
            break
  
#find the ifference of the 2 lists
set_difference = set(xmaslist[preamble:]) - set(answerlist)
print('sd', set_difference)

