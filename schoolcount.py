inp = input('Enter a file name: ')
file = open(inp)
school = dict()
for line in file :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    str = line.split()
    email = str[1]
    at = email.find('@')
    sp = email.find(' ' , at)
    sch = email[at + 1 : sp]
    school[sch] = school.get(sch , 0) + 1
print(school)
