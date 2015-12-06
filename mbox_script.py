fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1 :
        continue
##    if line.startswith('From:') :
    print(line)


##fhand = open('mbox.txt')
##count = 0
##for line in fhand:
##    count = count + 1
##print('Line Count:', count)

