## Exercise 6: Use your code from the practice exercise at the end of module 11 that
## asks for a first and last name and hourly rate. Then parse and print the last name
## then first name. This would be a sample if I ran it on my name.

name = input('Enter your first and last name: ')
rate = input('Enter your hourly rate: ')

namelen = len(name)
blanklen = name.find(' ')
lastname = name[blanklen+1:namelen]
firstname = name[0:blanklen]
annual = float(rate) * 2080.0
print('Name: ' ,lastname,',',firstname,' Hourly: $',rate,' Annual: $',annual)

