import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
data = urllib.request.urlopen(url)
j = data.read().decode()
info = json.loads(j)

print('Retrieving', url)
print('Retrieved' , len(j) , 'characters')

sum = 0
count = 0
for item in info["comments"]:
    num = item['count']
    sum = sum + int(num)
    count = count + 1
print('Count:' , count)
print('Sum:' , sum)
