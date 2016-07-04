import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
url = raw_input("Enter URL: ")
if url is '':
    url = 'http://python-data.dr-chuck.net/comments_42.xml'

tree = ET.fromstring(url)
names = ET.findall('comments/comment')
sum = 0
# <comment>
#    <name>Romina</name>
#    <count>97</count>
# </comment>
for i in names:
    sum = sum + int(i.find('count').text)

print sum

# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break
#
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
#     print data
#     tree = ET.fromstring(data)
#
#
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
#
#     print 'lat',lat,'lng',lng
#     print location
