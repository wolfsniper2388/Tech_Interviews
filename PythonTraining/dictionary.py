''' Create a dictionary from scratch using SQLite3 as the backing store.
    Multi-language, concurrent (with real locks)
        dict
        ----
        key TEXT    (primary key, indexed and unique)
        value BLOB

Abstract Base Class:    MutableMapping
                        don't inherit from it first
                        we will inherit update() and __contains__, mark with XXX and use them when available
                        borrow codes from TupleDict and PersistentDict

SQL:    w3cschools.com/sql
        CREATE TABLE
        CREATE INDEX
        DELETE FROM
'''

import sqlite3
import collections
class SQLDict(collections.MutableMapping):
    'Persistent, concurrent dictionary based on SQL'
    # __setitem__   INSERT INTO
    # __getitem__   SELECT key
    # __delitem__   DELETE FROM
    # __len__       SELECT COUNT (*) FROM dict
    # __iter__      SELECT key 
    
    def __init__(self,dbname):
        self.conn=sqlite3.connect(dbname)
        c=self.conn.cursor()
        try:
            c.execute('CREATE TABLE dict (key text, value text)')
            # Index the table on the key
            c.execute('CREATE UNIQUE INDEX keyINDEX ON dict (key)')
        except sqlite3.OperationalError:
            pass
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.items())
        
    def __setitem__(self,key,value):
        # handle duplicate entries
        if key in self:     
            del self[key]
        item=key,value
        c=self.conn.cursor()
        c.execute('INSERT INTO dict VALUES (?,?)',item)
        self.conn.commit()
            
    def __getitem__(self,key):
        c=self.conn.cursor()
        t=(key,)
        c.execute('SELECT value FROM dict WHERE key=?',t)
        #Using fetchall()
        rows=c.fetchall()
        if not rows:
            raise KeyError(key)
        return rows[0][0]
        ''' Using fetchone()
        row=c.fetchone()
        #print row
        if row is None:
            raise KeyError(key)
        return row[0]
        '''
    def __delitem__(self,key):
        # XXX raise KeyError if missing
        if key not in self:
            raise KeyError(key)
        c=self.conn.cursor()
        t=(key,)
        c.execute('DELETE FROM dict WHERE key=?',t)
        self.conn.commit()
        
    def __len__(self):
        c=self.conn.cursor()
        c.execute('SELECT COUNT (*) FROM dict')
        rows=c.fetchall()
        return rows[0][0]
        
    def __iter__(self):
        c=self.conn.cursor()
        c.execute('SELECT key FROM dict')
        rows=c.fetchall()
        return iter([k for k, in rows])
            
    def close(self):
        self.conn.close()
    
    def __enter__(self):
        return self
    def __exit__(self,exctype,excinst,exctb):
        self.close()
        
# Testing SQLdict
d=SQLDict('Hettingers.db')
d['raymond']='red'
d['rachel']='blue'
d['matthew']='yellow'
print 'Raymond color is',d['raymond']
print 'Rachel color is',d['rachel']
print 'The number of records in SQLDict:', len(d)
del d['raymond']
print 'After deleting, the dict is', d
print 'keys in the dict are'
for k in d:
    print k

print '.items() are inherited from MutableMapping'    
print d.items()

with SQLDict('Hettingers.db') as e:
    print e['rachel']

