str = 'X-DSPAM-Confidence: 0.8475'
sp = str.find(' ')
end = str.find('5')
num = float(str[sp : end + 1])
print(num)
