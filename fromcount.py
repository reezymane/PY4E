inp = input('Enter a file name: ')
file = open(inp)
count = 0
for line in file :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    str = line.split()
    print(str[1])
    count = count + 1
print('There were' , count , 'lines in the file with From as the first word')
