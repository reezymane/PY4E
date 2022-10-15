import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html , 'html.parser')

import re
sum = 0
tags = soup('span')
for tag in tags :
    str = tag.decode()
    num = re.findall('[0-9]+' , str)
    if len(num) < 1 : continue
    for i in num :
        nn = int(i)
        sum = sum + nn
print(sum)
