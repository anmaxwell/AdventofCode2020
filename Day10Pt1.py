#read in the list of numbers
output = open("adapters.txt", "r")

#create the list to read in the adapters starting 0
adapterlist = [0]

#set counter for differences
ones = 0
twos = 0
threes = 0

#add each number to the list for comparison and count the length
for adapter in output:
    adapterlist.append(int(adapter.strip()))
    adapterlist.sort()

adapterlist.append(max(adapterlist)+3)

for i in range(len(adapterlist)-1):
    diff = adapterlist[i+1] - adapterlist[i]
    if diff == 1:
        ones +=1
    elif diff ==2:
        twos +=1
    else:
        threes +=1


print(ones, twos, threes)
print(ones*threes)