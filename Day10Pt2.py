import itertools as it
import more_itertools as mit


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
  
#iterate through the full list removing all combinations
#of the adapters.  
#only where adapters have consecutive indexes could there
#be an issue.
#identify combinations with consecutive indexes to check 

combocheck = []

for combo in posscombos:
    
    if len(combo) != 1:
        indexcheck = []
        #find the index of the adapters in the full list
        for removaladap in combo:
            indexcheck.append(adapterlist.index(removaladap))

        #check to see if consecutive and add to list to check further
        for i in range(len(indexcheck)-1):
            if indexcheck[i+1] - indexcheck[i] == 1:
                combocheck.append(indexcheck)
                break



#loop through all combos to check and find the indexes
#of the first and last consecutive groups.
#check that removing these adapters does not leave a gap 
#greater than 3

invalidcombos = []

for combo in combocheck:
    for group in mit.consecutive_groups(combo):
            indextocheck = list(group)
            if len(indextocheck) > 1:
                firstind = indextocheck[0]-1
                lastind = indextocheck[-1]+1
                if adapterlist[lastind] - adapterlist[firstind] >3:
                    invalidcombos.append(combo)
                    break

print(len(invalidcombos))

print('end', len(posscombos)-len(invalidcombos))

