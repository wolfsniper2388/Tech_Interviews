''' Teach how mixins work, what inheritance is really,
    how to use multiple inheritance, and how to use
    ABCs (abstract base classes) to impose discipline
    on mixins.

    This is all about code re-use    
    
    How to make a class iterable
        __iter__
        __getitem__ and __len__
        iter(func, sentinal)
        
    The issues with Mixins:
        cannot ask it programmatically what methods to implement (not introspectable)
        dones't check for the methods it needs
        easy to get wrong
    A good fix:
        a document the interface in an introspectable way
        a todo list: list of methods that need to be implemented
        only instantiate when the todo list is done
        
    Abstract Base Classes:
        Mixins with enforcement and introspection
'''
from abc import ABCMeta, abstractmethod

# Make a base class if the code will be re-used in subclasses
class Capper:
    'This is a mixin class'
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __len__(self):
        return 0
    
    @abstractmethod
    def __getitem__(self,index):
        raise IndexError
    
    
    def capitalize(self):
        return ''.join([c.upper() for c in self])

class UnCapper:
    'This is a mixin class'
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __len__(self):
        return 0
    
    @abstractmethod
    def __getitem__(self,index):
        raise IndexError
    
    
    def decapitalize(self):
        return ''.join([c.lower() for c in self])

from collections import Sequence
class DoubleSeq(Capper, UnCapper, Sequence):
    
    def __init__(self,seq):
        self.seq=seq
    
    def __len__(self):
        return (len(self.seq)+1) //2
    def __getitem__(self,index):
        if index>=len(self):
            raise IndexError("Index Error")
        return self.seq[index*2]
   
class TrippleSeq(Capper, Sequence):
    
    def __init__(self,seq):
        self.seq=seq
    
    def __len__(self):
        return (len(self.seq)+1) //3
    def __getitem__(self,index):
        if index>=len(self):
            raise IndexError("Index Error")
        return self.seq[index*3]

print 'Testing case of DoubleSeq and TrippleSeq'
d=DoubleSeq("Hettinger")
print d.capitalize()
print d.decapitalize()
t=TrippleSeq("Hettinger")
print t.capitalize()
    
    
# Make a dictionary based on the file system
import os
import collections
import json

class PersistentDict(collections.MutableMapping):
    def __init__(self,dirname):
        self.dirname=dirname
        try:
            os.mkdir(dirname)
        except OSError:
            pass
    
    def __setitem__(self,key,value):
        fullname=os.path.join(self.dirname,key)
        with open(fullname,'wb') as f:
            f.write(json.dumps(value))
            
    def __getitem__(self,key):
        fullname=os.path.join(self.dirname,key)
        try:
            with open(fullname,'r') as f:
                return f.read()
        except OSError:
            pass
    def __delitem__(self,key):
        fullname=os.path.join(self.dirname,key)
        try:
            os.remove(fullname)
        except OSError:     # normal dictionary returns KeyError if the file doesn't exist
            raise KeyError(key)
    
    def __len__(self):    
        return len(os.listdir(self.dirname))
    
    def __iter__(self):    
        return iter(os.listdir(self.dirname))

print 'Testing case of PersistentDict'       
p=PersistentDict("Hettingers")
p['raymond']='red'
p['rachel']='blue'
p['matthew']='yellow'
print 'Raymond color is', p['raymond']
print 'Rachel color is', p['rachel']
print 'length of Hettingers is', len(p)
for k in p:
    print k


# Implementing a self-definded object from scratch

class TupleDict(collections.MutableMapping):
    ''' Dictionary-like object based on a list of tuples.
        It is more space-efficient
        It doens't require keys to be hashable
        It remembers the order keys added 
    '''
    #__repr__,__setitem__, __getitem__, delitem__, __len__, __iter__
    
    def __init__(self,lot=[],**kwds):
        self.lot=[]
        self.update(lot,**kwds)
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.lot)
    
    def __len__(self):
        return len(self.lot)
    
    # each time an item is indexed/searched, move the item one position forward if it's not the first in the dict
    def __getitem__(self,key):
        for i,t in enumerate(self.lot):
            k,v =t      #unpack the item
            if k==key:
                if i:       #if the item is not in the optimal position, swap it
                    self.lot[i],self.lot[i-1]=self.lot[i-1],self.lot[i]
                return v
        raise KeyError(key)
    
    def __setitem__(self,key,value):
        if key in self:     # in calls self.__contains__(key), which further calls self[key]--the __getitem__ notice 
                            # don't use: if key in self.lot
            del self[key]
        self.lot.append((key,value))
        
    def __delitem__(self,key):
        if key not in self:
            raise KeyError(key)
        self.lot=[t for t in self.lot if t[0]!=key]
    
    def __iter__(self):
        return iter([k for k,v in self.lot])        
        
        
print 'Testing case of TupleDict'    
t=TupleDict()
t['raymond']='red'
t['rachel']='blue'
t['matthew']='yellow'
print 'After Initializing, show repr function',t
print 'After Initializing, length of the tuple is', len(t)
t['rachel']='azure'
print 'After change value of one item',t

print 'get item in the dict'
print 'matthew color is', t['matthew']
print 'After adjusting position, t',t
print 'Rachel color is', t['rachel']
print 'delete item in the dict'
del t['raymond']
print 'Deleting Raymond', t.lot
print 'New constructor'
t1=TupleDict(raymond='red1',rachel='blue2')
t2=TupleDict([('raymond','red2'),('rachel','blue2')])
print 't1', t1
print 't2', t2