fname = raw_input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    words = line.split()
    for word in words:
        if word in lst: continue
        lst.append(word)
        #print word
lst.sort()
print lst
