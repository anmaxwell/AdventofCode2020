import cerberus
from cerberus import Validator


#read in the passport file
output = open("Passport.txt", "r")

schema = {'byr': {'required': True, 'type': 'integer', 'min': 1920, 'max': 2002},
            'iyr': {'required': True, 'type': 'integer', 'min': 2010, 'max': 2020},
            'eyr': {'required': True, 'type': 'integer', 'min': 2020, 'max': 2030},
            'pid': {'required': True, 'type': 'string', 'minlength': 9, 'maxlength': 9},
            'hgt': {'required': True, 'type': 'string', 'minlength': 4, 'maxlength': 5},
            'hcl': {'required': True, 'type': 'string', 'minlength': 7, 'maxlength': 7,'regex': '^#[0-9a-f]{6}'},
            'ecl': {'required': True, 'type': 'string', 'allowed': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']},
            'cid': {'required': False},
            }
v = Validator(schema)

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

        try:
            my_dict[key] = int(val)
        except ValueError:
            my_dict[key] = val

        if key == 'pid':
            my_dict[key] = val

    if v.validate(my_dict):
        height = my_dict['hgt']
        
        if height[-2:] == 'cm' and len(height)==5:
            hgtval = int(height[:3])
            if 150 <= hgtval <= 193:
                validpass +=1

        if height[-2:] == 'in' and len(height)==4:
            hgtval = int(height[:2])
            if 59 <= hgtval <= 76:
                validpass +=1


print(validpass)