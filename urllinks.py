# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter URL to start from: ')
if url is '':
    url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

def parseUrl(urlToParse,pos):
    html = urllib.urlopen(urlToParse).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    print "Retrieving: ", urlToParse
    tags = soup('a')

    currPos = 0
    for tag in tags:
        if currPos < pos-1 :
            currPos = currPos + 1
            continue
        #str = tag #.name #get('href', None)
        print "Name found: ", tag.string
        return tag.get('href', None)
############
i = 0
while i<count:
    url = parseUrl(url,position)
    i = i+1
