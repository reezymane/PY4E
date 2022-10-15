inp = input('Enter file: ')
file = open(inp)
words = list()
for line in file :
    line = line.rstrip()
    str = line.split()
    for inner in str :
        if inner not in words :
            words.append(inner)
        else : continue
words.sort()
print(words)
