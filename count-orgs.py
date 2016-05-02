import sqlite3
import re

# Connecting to the DB to store the results
conn = sqlite3.connect('organizations.sqlite')
cur = conn.cursor()

# Removing data, if exist
cur.execute('''DROP TABLE IF EXISTS Counts''')

# Creating a table to store data
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    # Find all From: lines in mailbox and extract domain names from emails
    domain = re.findall('^From: .*@(\S+)',line)
    if domain: # found
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain[0], ))
        row = cur.fetchone()
        if row is None: # Not yet in DB
            cur.execute('''INSERT INTO Counts (org, count)
                 VALUES ( ?, 1 )''', ( domain[0], ) )
        else : # Already in DB, increment counter
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                (domain[0], ))
conn.commit()
cur.close()
