import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit
conn.close()


conn = sqlite3.connect('example.db')
c = conn.cursor()

t=('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?',t)
#print c.fetchone()
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

# Way 1 to insert multiples rows
'''
for purchase in purchases:
    c.execute('INSERT INTO stocks VALUES(?,?,?,?,?)',purchase)
'''
# Way 2 to insert multiple rows, faster
c.executemany('INSERT INTO stocks VALUES(?,?,?,?,?)',purchases)



# Ways to GET data
nc=c.execute('SELECT * FROM stocks ORDER BY price')
# fetchone: one row at a time
print 'Using fetchone'
while True:
    row=nc.fetchone()
    if row is None:
        break
    print row

# fetchall: everything in memory all at once
print 'Using fetchall'
for row in nc.fetchall():
    print row

# Iterator: one row at a time
print 'Using iterator'
for row in nc:
    print row

#Iterator: using the two arguments form of iter()
print 'Using two-argument iterator'
for row in iter(nc.fetchone,None):
    print row
