#read in the instructions
output = open("instructions.txt", "r")

#set blank lists to monitor the steps and counts
command = []
value = []
linelist = []
i = 0
accumulator = 0


#read in each line, seperate the command and the value
for line in output:
    command.append((line.split()[0]))
    value.append(int(line.split()[1]))

#check for each unique run
while i not in linelist:
    linelist.append(i)

    if command[i] == 'jmp':
        i += value[i]
    elif command[i] == 'acc':
        accumulator += value[i]
        i +=1
    else:
        i +=1

print(accumulator)


