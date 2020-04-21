
import urllib.request
import xml.etree.ElementTree as ET

url = input('Please, enter URL:')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_349903.xml'

data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')
total = 0
for count in counts:
    total += int(count.text)

print ('total: ', total)
