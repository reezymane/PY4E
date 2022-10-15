inp = input('Enter a file name: ')
file = open(inp)
dow = dict()
for line in file :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    str = line.split()
    dow[str[2]] = dow.get(str[2] , 0) + 1
print(dow)
