## Exercise 1: Rewrite your pay computation script to give the employee
## 1.5 times the hourly rate for hours worked above 40 hours.
## The output should look like this:
## Enter Hours: 45
## Enter Rate: 10
## Pay: 475.0

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    overtime = hours - 40
    overtimepay = overtime*(1.5*rate)
    regularpay = 40*rate
    print('Pay:', regularpay+overtimepay)
else :
    pay = hours*rate
    print('Pay:', pay)
