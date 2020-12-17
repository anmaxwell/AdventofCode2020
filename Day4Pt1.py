
#read in the passport file
output = open("Passport.txt", "r")

#set number of valid passport to 0
validpass=0

#split the file into each passport
myarray = output.read().split("\n\n")
for line in myarray:
    partline = line.split()

    #create a blank dictionary
    my_dict = {}

    #take each item and put it in the dictionary
    for item in partline:
        (key, val) = item.split(':')
        my_dict[key] = val

    #check all the necessary fields are there
    if all (k in my_dict for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        validpass +=1

print(validpass)
