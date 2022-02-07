def main():
    
    #Open
    infile = open("philosophers.txt", "r")

    #Read
    #file_contents = infile.read()
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')

    #Print
    print(line1)
    print(line2)
    print(line3)

#Call Main
main()