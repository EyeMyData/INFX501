## Exercise 4: Download a copy of the file from www.py4inf.com/code/romeo.txt
## Write a program to open the file romeo.txt and read it line by line.
## For each line, split the line into a list of words using the split function.
## For each word, check to see if the word is already in a list. If the word
## is not in the list, add it to the list. When the program completes, sort and
## print the resulting words in alphabetical order.

fname = input('Enter file name: ')
fh = open(fname)
lst = list()                       # list for the desired output
for line in fh:                    
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           
        if element in lst:         
            continue               
        else :                     
            lst.append(element)        
lst.sort()                         
print(lst)                        
