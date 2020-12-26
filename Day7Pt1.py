#read in Rule
output = open("Rules.txt", "r")

#create a blank dictionary
bag_dict = {}

#set the bag colour to check for
colourcheck = ['shiny gold']

#create a list for the final count
finalcount = []

#create a dictionary of bags and remove unecessary characters
for line in output:
    line=line.strip()

    bagrules = line.split("contain")

    mainbag=bagrules[0].rstrip(' bags')
    subbags=bagrules[1].split(',')

    for i in range(len(subbags)):
        subbags[i]=subbags[i][3:].rstrip(' bags.')

    bag_dict[mainbag] = subbags

#loop through to check each level of bags
while len(colourcheck) != 0:
    newcheck=[]
    for item in bag_dict.items():
        for colour in colourcheck:
            if colour in item[1]:
                newcheck.append(item[0])
                finalcount.append(item[0])
    colourcheck=newcheck

print(len(set(finalcount)))
