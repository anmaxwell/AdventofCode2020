import cerberus
from cerberus import schema_registry


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

        schema = {'byr': {'type': 'integer', 'min': 10}, 
                    'hgt': {'type': 'integer', 'min': 10}}
        v = Validator(schema)
        v.validate(my_dict)

        validpass +=1

print(validpass)
