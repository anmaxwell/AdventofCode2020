
#read in the treemap
treemap = open("treepos.txt", "r")

#set counters
notrees = 0
currpos = 0

#loop through each line in the file and find if there is a tree in the poosition 
for ind, arow in enumerate(treemap):

    rowlen = len(arow)-1

    #calc what position to check
    poscheck = currpos%rowlen

    if ind%2 == 0:

        #if it's a tree then count
        if arow[poscheck] == '#':
            print(arow)
            notrees +=1
        
        #move along
        currpos +=1


print(notrees)


        

    



 
