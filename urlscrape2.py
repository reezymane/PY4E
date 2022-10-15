import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
c = input('Enter count: ')
p = input('Enter position: ')
ic = int(c)
ip = int(p) - 1

print('Retrieving:' , url)

while ic > 0 :
    links = list()
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html , 'html.parser')
    tags = soup('a')
    for tag in tags :
        link = tag.get('href' , None)
        links.append(link)
    print('Retrieving:' , links[ip])
    url = links[ip]
    ic = ic - 1
