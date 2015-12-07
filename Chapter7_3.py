## Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, 
## they add a harmless Easter Egg to their program (en.wikipedia.org/wiki/Easter_egg_(media)).
## Modify the program that prompts the user for the file name so that
## it prints a funny message when the user types in the exact file name 'na boo'. The 
## program should behave normally for all other files which exist and don't exist. Here 
## is a sample execution of the program:
## python egg.py
## Enter the file name: mbox.txt
## There were 1797 subject lines in mbox.txt
## python egg.py
## Enter the file name: missing.tyxt
## File cannot be opened: missing.tyxt
## python egg.py


fname = input('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    if fname.upper() == "NA NA BOO BOO":
        print("NA NA BOO BOO TO YOU - You've been punked!")
    else:
        print("File cannot be opened: ", fname)
    quit()    
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
output = "There were {0} subject lines in {1}.".format(str(count), fname )
print(output)
