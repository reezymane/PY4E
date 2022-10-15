inp = input('Enter a file name: ')
file = open(inp)
dow = dict()
for line in file :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    str = line.split()
    dow[str[1]] = dow.get(str[1] , 0) + 1
email = None
count = None
for e , c in dow.items() :
    if count is None or c > count :
        email = e
        count = c
print(email , count)
