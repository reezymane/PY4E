score = input('Enter score: ')
def computegrade (grade) :
    if grade < 0 or grade > 1.0 :
        print('Bad score')
    elif grade >= 0.9 :
        print('A')
    elif grade >= 0.8 :
        print('B')
    elif grade >= 0.7 :
        print('C')
    elif grade >= 0.6 :
        print('D')
    else :
        print('F')
try :
    score = float(score)
    computegrade (score)

except :
    print('Bad score')
