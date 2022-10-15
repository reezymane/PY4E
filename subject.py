file = input('Enter a file name: ')
count = 0
if file == 'na na boo boo' :
    print(file.upper() , "TO YOU - You have been punk'd!")
    quit()
try :
    inp = open(file)
except :
    print('File cannot be opened:' , file)
    quit()
for line in inp :
    if line.startswith('Subject:') :
        count = count + 1
print('There were' , count , 'subject lines in' , file)
