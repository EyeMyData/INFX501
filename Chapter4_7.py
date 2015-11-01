## Exercise 7: Rewrite the grade program from the previous chapter using a function
## called computegrade that takes a score as its parameter and returns a grade as a
## string. Use the following data. Run the program repeatedly to test the various
## different values for input.
## Score Grade
## >= 0.9 A
## >= 0.8 B
## >= 0.7 C
## >= 0.6 D
## < 0.6 F

def computegrade(score):
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

score = input('Enter Score between 0.0 and 1.0: ')
computegrade(score)
