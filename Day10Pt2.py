#read in the list of numbers
output = open("adapters.txt", "r")

#create the list to read in the adapters starting 0
adapterlist = [0]

#create the adapter list
for adapter in output:
    adapterlist.append(int(adapter.strip()))
    adapterlist.sort()

adapterlist.append(max(adapterlist)+3)
