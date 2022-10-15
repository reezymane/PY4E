import re
inp = input('Enter file name: ')
file = open(inp)
sum = 0
for line in file :
    line = line.rstrip()
    num = re.findall('[0-9]+' , line)
    if len(num) < 1 : continue
    for n in num :
        i = int(n)
        sum = sum + i
print(sum)
