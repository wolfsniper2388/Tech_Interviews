''' Get familiar with list comprehension
'''

lot=[('raymond','red'),('rachel','blue'),('matthew','blue')]

# 1. make: ['raymond','rachel','mathew']
print '1'
print [name for name,color in lot]
print [t[0] for t in lot]
from operator import itemgetter
print map(itemgetter(0),lot)

# 2. Give: key='rachel', find the value 'blue'
print '2'
key='rachel'
print [color for name,color in lot if name==key]
print [t[1] for t in lot if t[0]==key]

# 3. Give: key='rachel', make this: [('raymond','red'),('matthew','blue')]
print '3'
key='rachel'
print [(name,color) for name,color in lot if name!=key]

# 4. Given key='roger' and value='orange' make this: [('raymond','red'),('rachel','blue'),('matthew','blue'), ('roger','orange')]
print '4'
key='roger'
value='orange'
lot.append((key,value))
print lot

# 5. Make an iterator over the tuples
it=iter(lot)

    
# 6. Make an iterator over the tuples
it=iter([name for name,color in lot])


# Pickling
print '\nUsage of pickel'
import pickle
hansolo=[10,20,30,{'rachel':'blue'}]
c=pickle.dumps(hansolo)
print 'After pickling to string, hansolo has a type of', type(c)
hansolo_recovery=pickle.loads(c)
print 'After pickling back, hansolo has a type of', type(hansolo_recovery)