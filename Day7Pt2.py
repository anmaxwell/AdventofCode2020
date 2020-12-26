#read in Rule
output = open("Rules.txt", "r")

#create a blank dictionary
bag_dict = {}

#set the bag colour to check for
colourcheck = ['shiny gold']

#create a count for the number of bags
finalcount = 0

#create a dictionary of bags and remove unecessary characters
for line in output:
    line=line.strip()

    bagrules = line.split("contain")

    mainbag=bagrules[0].rstrip(' bags')
    subbags=bagrules[1].split(',')

    for i in range(len(subbags)):
        subbags[i]=subbags[i].rstrip(' bags.').lstrip()

    bag_dict[mainbag] = subbags

#loop through to check each level of bags
while len(colourcheck) != 0:
    newcheck=[]

    #work out how many bags of each colour and repeat the count for each one
    #definitley not the best solution
    for colour in colourcheck:
        for eachbag in bag_dict[colour]:
            if eachbag != 'no other':
                bagcount=int(eachbag[0])
                finalcount += bagcount
                for i in range(bagcount):
                    newcheck.append(eachbag[2:])
    colourcheck=newcheck

print(finalcount)