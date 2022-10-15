total = 0
count = 0
while True :
    num = input('Enter a number: ')
    if num == 'done' :
        break
    else :
        try :
            num = int(num)
            count = count + 1
            total = total + num
        except :
            print('Invalid input')
print(total , count , total/count)
