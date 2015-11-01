## Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
## and create a function called computepay which takes two parameters
## (hours and rate). This would be the output:
## Enter Hours: 45
## Enter Rate: 10
## Pay: 475.0

def computepay(hours,rate):
    print('Enter Hours: ', hours)
    print('Enter Rate: ', rate)
    if hours > 40:
        overtime = hours - 40
        overtimepay = overtime*(1.5*rate)
        regularpay = 40*rate
        print('Pay:', regularpay+overtimepay)
    else :
        pay = hours*rate
        return('Pay:', pay)
computepay(45,10)
