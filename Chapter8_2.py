## Exercise 2: Figure out which line of the above program is still not properly
## guarded. See if you can construct a text file which causes the program to fail and
## then modify the program so that the line is properly guarded and test it to make
## sure it handles your new text file.

fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print("File not found:", fname)
    quit()
try:
    for line in fhand:
        words = line.split()
        if len(words) == 0 : continue
        if words[0] != 'From' : continue
        print(words[2])
except:
    print("File:", fname,"contains no data.")
    quit()
