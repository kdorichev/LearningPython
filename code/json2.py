import json
import urllib

url = raw_input('URL: ')
if url == '':
    url = 'http://python-data.dr-chuck.net/comments_42.json'

print 'Retrieving', url
uh = urllib.urlopen(url)
info = uh.read()
print 'Retrieved',len(info),'characters'
#print info

info = json.loads(info)

sum = 0
print "Count: ", len((info['comments']))

for i in info['comments']:
    sum = sum + int(i['count'])
print 'Sum: ', sum
