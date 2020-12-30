#start with how many paths make up the first step then build 
#on to how many paths make it to the next step and continue
#to sum all the previous paths

#read in the list of numbers
output = open("adapters.txt", "r")

#create the list to read in the adapters starting 0
adapterlist = [0]

#create the adapter list
for adapter in output:
    adapterlist.append(int(adapter.strip()))

adapterlist.append(max(adapterlist)+3)
adapterlist.sort()

paths = [0]*(max(adapterlist)+1)
paths[0] = 1


for index in range(1, max(adapterlist)+1):
    for x in range(1,4):
        if (index - x) in adapterlist:
            paths[index] += paths[index - x]

print(paths)

print("solution " + str(paths[-1]))