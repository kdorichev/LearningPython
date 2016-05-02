# This script parses the mailbox and calculates the average spam confidense value
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
spam = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(':')
    strnumber = line[pos+1:]
    strnumber = strnumber.strip()
    spam = spam + float(strnumber)

print "Average spam confidence: ",spam/count
