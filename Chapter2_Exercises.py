
## Exercise 2: Write a program that uses input() to prompt a user for
## their name and then welcomes them.
name = input('Enter your name: ')
print('Hello ' + name)


## Exercise 3: Write a program to prompt the user for hours and rate
## per hour to compute gross pay.
hours = float(input('Enter hours worked: '))
rate = float(input('Pay rate without $: '))
pay = hours*rate
print(pay)

## Exercise 4: Assume that we execute the following assignment statements:
## width = 17
## height = 12.0

## For each of the following expressions, write the value of the expression
## and the type (of the value of the expression).
## 1. width/2
## 2. width/2.0
## 3. height/3
## 4. 1+2*5

width = 17
height = 12.0

print(width/2)
print(type(width/2))

print(width/2.0)
print(type(width/2.0))

print(height/3)
print(type(height/3))

print(1+2*5)
print(type(1+2*5))


## Exercise 5: Write a program which prompts the user for a Celsius temperature,
## convert the temperature to Fahrenheit and print out the converted temperature.

celsius = float(input('Please provide a Celsius temperature:'))
fahrenheit = (celsius * 1.8) + 32
print('This means it is',fahrenheit,'degrees Fahrenheit')

