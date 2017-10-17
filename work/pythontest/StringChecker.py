#user input string
STR_IN = raw_input("Enter A String In Caps\n")
#count = a + b
#dna check function
def DNAcheck(string):
    print "Checking for DNA"
    #counter
    count = 1
    #add to counter when certain letters are seen
    for i in range(1, len(string)):
        if string[i] == "T":
            count = count + 1
        if string[i] == "G":
            count = count + 1
        if string[i] == "C":
            count = count +1
        if string[i] == "A":
            count = count + 1
    #print count
    #print len(string)
#check to see if the length of string is equal to counter
    if count == len(string):
        print "yes"
    else:
        print "no"
#rna check function
def RNAcheck(string):
    print "Checking for RNA"
    #counter
    count = 1
    #add to counter when certain letters are seen
    for i in range(1, len(string)):
        if string[i] == "C":
            count = count +1
        if string[i] == "U":
            count = count +1
        if string[i] == "G":
            count = count +1
        if string[i] == "A":
            count = count +1
    #print count
    #print len(string)
#check to see if the length of string is equal to counter
    if count == len(string):
        print "yes"
    else:
        print "no"
#protein check function
def PROcheck(string):
    print "Checking for Protein"
    #counter
    count = 1
    #add to counter when certain letters are seen
    for i in range(1, len(string)):
        if string[i] == "F":
            count = count +1
        if string[i] == "L":
            count = count +1
        if string[i] == "I":
            count = count +1
        if string[i] == "M":
            count = count +1
        if string[i] == "V":
            count = count +1
        if string[i] == "S":
            count = count +1
        if string[i] == "P":
            count = count +1
        if string[i] == "T":
            count = count +1
        if string[i] == "A":
            count = count +1
        if string[i] == "Y":
            count = count +1
        if string[i] == "O":
            count = count +1
        if string[i] == "H":
            count = count +1
        if string[i] == "Q":
            count = count +1
        if string[i] == "N":
            count = count +1
        if string[i] == "K":
            count = count +1
        if string[i] == "D":
            count = count +1
        if string[i] == "E":
            count = count +1
        if string[i] == "C":
            count = count +1
        if string[i] == "W":
            count = count +1
        if string[i] == "R":
            count = count +1
        if string[i] == "G":
            count = count +1
    #print count
    #print len(string)
#check to see if the length of string is equal to counter
    if count == len(string):
        print "yes"
    else:
        print "no"
#run functions
THIS = 0
DNAcheck(STR_IN)
RNAcheck(STR_IN)
PROcheck(STR_IN)
