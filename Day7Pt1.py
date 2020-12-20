#read in Rule
output = open("Rules.txt", "r")

#create list of responses
for line in output:
    line=line.strip()

    bagrules = line.split("contain")

    #create a blank dictionary
    bag_dict = {}

    mainbag=bagrules[0].replace(' bags', '')
    subbags=bagrules[1].split(',')

    for singlebag in subbags:
        if mainbag in bag_dict:
            bag_dict[mainbag].append('singlebag')
        else:
            bag_dict[mainbag] = singlebag

        



    print(bag_dict)



