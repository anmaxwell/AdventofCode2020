import itertools as it


#read in the list of numbers
output = open("adapters.txt", "r")

#create the list to read in the adapters starting 0
adapterlist = [0]

#create the adapter list
for adapter in output:
    adapterlist.append(int(adapter.strip()))
    adapterlist.sort()

adapterlist.append(max(adapterlist)+3)

#find all the adapters that could be removed
#ie leave a difference of 3 or less if removed

removallist = []
for i in range(1, len(adapterlist)-1):
    if adapterlist[i+1] - adapterlist[i-1] < 4:
        removallist.append(adapterlist[i])

#find out all the possible combinations that could be removed

posscombos = []
for n in range(1, len(removallist) + 1):
    for combination in it.combinations(removallist, n):
        posscombos.append(combination)
  
#iterate through the full list removing all combintions
#of the adapters that can be removed to see if they leave
#a valid combination.  
#individual adapters will be valid, only where adapters have 
#consecutive indexes could there be an issue.
#identify combinations with consecutive indexes

validcombos = 0
combocheck = []

for combo in posscombos:
    
    if len(combo) == 1:
        validcombos +=1
    else:
        indexcheck = []
        #find the index of the adapters in the full list
        for removaladap in combo:
            indexcheck.append(adapterlist.index(removaladap))

        print('check', indexcheck)

        #check to see if consecutive
        
        for i in range(len(indexcheck)-1):
            if indexcheck[i+1] - indexcheck[i] == 1:
                combocheck.append(indexcheck)
                break


    print('more checking', combocheck)
print('end', validcombos)





