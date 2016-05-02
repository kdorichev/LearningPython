# THis scrip reads the data from text file, extracts numbers and
# calculates thier sum
# Written by K. Dorichev 2016-04-24
import re

fname = raw_input("Enter filename to parse: ")
if not fname :
    fname = 'regex_sum_268216.txt'

#try:
fh = open(fname)
#except Exception as e:
#    raise

sum = 0
for line in fh:
    numbersList = re.findall('[0-9]+',line)
    if not numbersList: continue
    for numberStr in numbersList:
        sum = sum + int(numberStr)
print sum
