inp = input('Enter a file name: ')
file = open(inp)
hc = dict()
for line in file :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    str = line.split()
    time = str[5]
    hour = time[:2]
    hc[hour] = hc.get(hour , 0) + 1
for k , v in sorted(hc.items()) :
    print(k , v)
