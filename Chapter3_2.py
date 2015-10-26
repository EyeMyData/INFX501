## Exercise 2: Rewrite your pay program using try and except so that your
## program handles non-numeric input gracefully by printing a message
## and exiting the program. The following shows the output from three
## executions of the program:

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        overtime = hours- 40
        overtimepay = overtime*(1.5*rate)
        regularpay = 40*rate
        print('Pay:', regularpay+overtimepay)
    else :
        pay = hours*rate
        print('Pay:', pay)
except: 
    print('Please enter a number')
