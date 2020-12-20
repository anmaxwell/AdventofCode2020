from collections import Counter


#read in declarations
output = open("declarations.txt", "r")

#create list of responses
myarray = output.read().split("\n\n")

#set counter to 0
count = 0

#loop through each declaration 
for item in myarray:

    #calc the number in the group
    nacount=0
    for letter in item:
        if letter == '\n':
            nacount +=1
    groupcount = nacount+1

    #remove new line character
    item = item.replace('\n',"")
    alllets = set(item)

    deccount = Counter(item)

    for letter in alllets:
        nocc = deccount[letter]
        if nocc == groupcount:
            count +=1
        
print(count)

