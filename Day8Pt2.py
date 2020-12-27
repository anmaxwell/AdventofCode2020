#read in the instructions
output = open("instructions.txt", "r")

#set blank lists to hold the instrutions and values
command = []
value = []

#set counts
nopcount = 0
jmpcount = 0
filelen = 0
jmptochange = 0
noptochange = 0
finalval = 0

#read in each line, seperate the command and the value
for line in output:
    command.append((line.split()[0]))
    value.append(int(line.split()[1]))
    if line.split()[0] == 'nop':
        nopcount +=1
    if line.split()[0] == 'jmp':
        jmpcount +=1
    filelen +=1

#work through changing each nop in order to see if it breaks the loop
while noptochange < nopcount:

    #set up the counts to look for the infinite loop
    linelist = []
    i = 0
    accumulator = 0
    nopcounter = 0

    #check for each unique run
    while i not in linelist:
        linelist.append(i)
           
        if command[i] == 'jmp':
            i += value[i]           
        elif command[i] == 'acc':
            accumulator += value[i]
            i +=1 
        elif command[i] == 'nop' and nopcounter == noptochange:
            i += value[i]
            nopcounter +=1        
        else:
            i +=1
            nopcounter +=1          
        
        if i == filelen:
            finalval = accumulator
            break

    noptochange +=1
    if finalval != 0:
        break

#work through changing each jmp in order to see if it breaks the loop
while jmptochange < jmpcount:

    #set up the counts to look for the infinite loop
    linelist = []
    i = 0
    accumulator = 0
    jmpcounter = 0

    #check for each unique run
    while i not in linelist:
        linelist.append(i)
           
        if command[i] == 'jmp' and jmpcounter == jmptochange:
                    i +=1
                    jmpcounter +=1            
        elif command[i] == 'jmp' and jmpcounter != jmptochange:
                    i += value[i]
                    jmpcounter +=1            
        elif command[i] == 'acc':
                    accumulator += value[i]
                    i +=1            
        else:
                    i +=1            
        
        if i == filelen:
            finalval = accumulator
            break

    jmptochange +=1
    if finalval != 0:
        break

print('answer', finalval)


