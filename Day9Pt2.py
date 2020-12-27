#read in the list of numbers
output = open("xmaslist.txt", "r")

result = 1504371145
#result = 127
filelen = 0

#create the blank list to read the file
xmaslist = []

#add each number to the list for comparison and count the length
for item in output:
    xmaslist.append(int(item.strip()))
    filelen +=1

#loop through the list of numbers
for i in range(filelen):
    #set sum to 0 and create blank list for numbers in sequence
    sumvals = 0
    answerlist = []
    #continue to add numbers to get to the result we need
    while sumvals < result:
        sumvals += xmaslist[i]
        answerlist.append(xmaslist[i])
        i +=1
  
    #stop if the number matches
    if sumvals == result:
        break

#add the min and max numbers in the list
answer = max(answerlist)+min(answerlist)
print(answer)