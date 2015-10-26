## Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
## If the score is out of range print an error. If the score is between 0.0
## and 1.0, print a grade using the following table:
## Score Grade
## >= 0.9 A
## >= 0.8 B
## >= 0.7 C
## >= 0.6 D
## < 0.6 F

score = input('Enter Score between 0.0 and 1.0: ')

try:
    float(score)
    if float(score) >= 0.0 and float(score) <= 1.0:
        try:
            score = float(score)
            if score >= 0.9:
                print('A')
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            elif score < 0.6:
                print('F')
        except: 
            print('Bad score')
    if float(score) < 0.0 or float(score) > 1.0:
        print('Bad score')
except ValueError:
    print('Bad score')

