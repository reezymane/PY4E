file = input('Enter a file name: ')
inp = open(file)
count = 0
total = 0
for line in inp :
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') :
        spam = float(line[20:])
        count = count + 1
        total = total + spam
print('Average spam confidence:' , total/count)
