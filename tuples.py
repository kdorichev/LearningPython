import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# Building a gistogram based on a dictionary
d = dict()
hour = ''
for line in handle:
    if not re.findall('^From ',line): continue
    words = line.split()
    hour =  re.findall('^([0-9][0-9]):',words[5])
    hr = hour[0]
    d[hr] = d.get(hr,0) +1

# Create a List and sort it
lst = list()
for v,k in d.items():
    lst.append( (v,k) )
    lst.sort()

# Print the list
for v,k in lst:
    print v,k
