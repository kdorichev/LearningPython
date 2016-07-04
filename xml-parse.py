import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
url = raw_input("Enter URL: ")
if url is '':
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
print url
xml = urllib.urlopen(url).read()

tree = ET.fromstring(xml)
names = tree.findall('comments/comment')

sum = 0
# <comment>
#    <name>Romina</name>
#    <count>97</count>
# </comment>
for i in names:
    sum = sum + int(i.find('count').text)

print sum
