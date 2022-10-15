file = input('Enter a file name: ')
inp = open(file)
for line in inp :
    line = line.rstrip()
    line = line.upper()
    print(line)
