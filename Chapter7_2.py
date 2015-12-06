## Exercise 2: Write a program to prompt for a file name, and then read through the
## file and look for lines of the form:
## X-DSPAM-Confidence:  0.8475

text = input('Enter a file name:')
fhand = open(text)
for line in fhand:
    line = line.rstrip()
    print(line.upper())

    
##    if line.startswith('From:') :
    
##fhand = open('mbox.txt')
##count = 0
##for line in fhand:
##    count = count + 1
##print('Line Count:', count)

