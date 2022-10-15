import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

input = input('Enter location: ')
uh = urllib.request.urlopen(input)
text = uh.read().decode()
stuff = ET.fromstring(text)
lst = stuff.findall('comments/comment')

print('Retrieving' , input)
print('Retrieved' , len(text) , 'characters')

sum = 0
for x in lst :
    num = x.find('count').text
    sum = int(num) + sum

print('Count:' , len(lst))
print('Sum:' , sum)
