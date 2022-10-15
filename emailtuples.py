inp = input('Enter a file name: ')
file = open(inp)
dow = dict()
for line in file :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    str = line.split()
    dow[str[1]] = dow.get(str[1] , 0) + 1
emails = list()
for key , value in dow.items() :
    emails.append((value , key))
emails = sorted(emails , reverse = True)
for value , key in emails[:1] :
    print(key , value)
