def main():
    #Open for Write
    outfile = open("philosophers.txt", "w")

    #Write Names
    outfile.write("John Locke" + '\n')
    outfile.write("David Hume" + '\n')
    outfile.write("Edmund Burke" + '\n')

    #Close
    outfile.close()

def add_my_name():
        outfile = open("philosophers.txt", "a")

        #Write My name
        outfile.write("Collin Covington\n")

        #Close
        outfile.close()
    
main()
add_my_name()
