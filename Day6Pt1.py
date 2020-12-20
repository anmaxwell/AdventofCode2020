#read in declarations
output = open("declarations.txt", "r")

#create list of responses
myarray = output.read().split("\n\n")

#set counter to 0
count = 0

#loop through each declaration and add to count
for item in myarray:
    item = item.replace('\n',"")
    count += (len(set(item)))

print(count)

