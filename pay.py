def computepay (hours, rate) :
    if hours > 40 :
        pay = (hours - 40) * (1.5 * rate) + (40 * rate)
        return pay
    else :
        pay = hours * rate
        return pay

h = input('Enter Hours: ')
try :
    h = int(h)
    r = input('Enter Rate: ')
    try :
        r = float(r)
        p = computepay (h, r)
        print('Pay' , p)
    except :
        print('Error, please enter numeric input')
except :
        print('Error, please enter numeric input')
