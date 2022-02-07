    #Open
infile = open("clients.txt", 'r')

    #For Loop
counter = 1
for client in infile:
    print(counter,". ", client.rstrip('\n'), sep="")
    counter += 1
        

