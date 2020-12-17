
#read in the passwords
psswdlist = open("passwords.txt", "r")
novalid = 0

#loop through each line in the file and split the line to 3 sections
for aline in psswdlist:
    values = aline.split()

    #find the min and max count needed
    firstpos = int(values[0].split('-')[0])-1
    lastpos = int(values[0].split('-')[1])-1

    #find the letter to be searched on
    refletter = values[1][0]

    #set the character count to zero
    validmatch = 0

    #count if the character postion match is true
    if values[2][firstpos] == refletter:
        validmatch +=1
    if values[2][lastpos] == refletter:
        validmatch +=1
    
    #count if valid password
    if validmatch == 1:
        novalid +=1

print(novalid)
 
