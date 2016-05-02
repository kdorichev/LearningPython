import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

# HTTP/1.1 200 OK
# Date: Mon, 25 Apr 2016 07:36:30 GMT
# Server: Apache
# Last-Modified: Mon, 12 Oct 2015 14:55:29 GMT
# ETag: "20f7401b-1d3-521e9853a392b"
# Accept-Ranges: bytes
# Content-Length: 467
# Cache-Control: max-age=604800, public
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Headers: origin, x-requested-with, content-type
# Access-Control-Allow-Methods: GET
# Connection: close
# Content-Type: text/plain
#
# Why should you learn to write programs?
#
# Writing programs (or programming) is a very creative
#
# and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# a difficult data analysis problem to having fun to helping
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program, and that once
# you know how to program you will figure out what you want
# to do with your newfound skills.
