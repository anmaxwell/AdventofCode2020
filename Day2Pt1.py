
#read in the passwords
psswdlist = open("passwords.txt", "r")
novalid = 0

#loop through each line in the file and split the line to 3 sections
for aline in psswdlist:
    values = aline.split()

    #find the min and max count needed
    minletcount = values[0].split('-')[0]
    maxletcount = values[0].split('-')[1]

    #find the letter to be searched on
    refletter = values[1][0]

    #count occurences of letter in password
    actcount = values[2].count(refletter)

    #find number of valid passwords
    if int(minletcount) <= int(actcount) <= int(maxletcount):
        novalid +=1

print(novalid)
 
