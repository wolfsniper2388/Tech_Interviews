''' Develop sophisticated understading of property

Benifits of property() for computed fields:
    reduce data size
    imporve data consistency
    cleaner API
    create read-only attributes
    
Debugging techniques:
    use a setter to check values (type, range, etc) to detect data corruption at the moment it occurs
    module of validators:
        validate_percentage
        check_range
'''

from __future__ import division

#Put this in a module called validators
def validate_percentage(value):
    if not isinstance(value,(int,float)):
        raise TypeError('must be an int or float')
    if value<0 or value>100:
        raise ValueError('must be a percentage')

def is_low_smaller(low,high):
    if low<=high:
        return True
    else:
        return False
    

class PriceRange(object):
    
    def __init__(self,low,high):
        self.low=low
        self.high=high
  
    
    @property       #midpoint=property(midpoint)
    def midpoint(self):
        return (self.low+self.high)/2
    
    def recenter(self,new_midpoint):
        'Move the low and the high to keep the distance the same'
        half_dist=(self.high-self.low)/2
        self.low=new_midpoint-half_dist
        self.high=new_midpoint+half_dist
    
    #managed property
    @property
    def low(self):
        return self._low        #it's wrong to use self.low as it will cause infinite loop
    @property    
    def high(self):
        return self._high
    
    @low.setter
    def low(self,new_low):
        validate_percentage(new_low)
        
        self._low=new_low
   
    @high.setter
    def high(self,new_high):
        validate_percentage(new_high)
       
        self._high=new_high
    
    
        
p=PriceRange(10,20)
print 'dict of p is:',p.__dict__
print 'low is',p.low
print 'high is',p.high
print 'midpoint is',p.midpoint

p.recenter(16)

print 'low is',p.low
print 'high is',p.high
print 'midpoint is',p.midpoint  #the new midpoint is calculated dynamically

p.high=30
print 'low is',p.low
print 'high is',p.high
print 'midpoint is',p.midpoint  #the new midpoint is calculated dynamicallys



