''' Circuitous (tm) An advanced circle analytic company '''

import math
from collections import namedtuple

PI=math.pi
Version=namedtuple('Version',['major','mior'])


class Circle(object):   #new-style class
    'An advanced circle analytic toolkit'   #class-variable is for data that is shared by all instance
    
    __slots__ = 'diameter'      #Fly-weight design pattern implemented by suppressing the instance 
    
    
    
    version=Version(0,3)            #named tuple for clarity and avoid floating point comparison issues
        
    def __init__(self,radius):
        self.radius=radius      #instance variable is for data that is unique for each instance
    
    def __repr__(self):     #write this method to improve debugging
        #return 'Circle(%r)' % self.radius    #wrong way of doing this
        return '%s(%r)' % (self.__class__.__name__, self.radius)    #self is the class itself and the children classes as well
    
    def area(self):     #regular method
        'Return the area of circle'
        p=self.__perimeter()        #class local reference - sometime you need "self" to actually be you
        r=p/2.0/PI
        return PI * r **2.0
    
    def perimeter(self):
        'Return the perimeter of circle'
        return 2*PI*self.radius
    __perimeter=perimeter       #name mangling to keep a local copy
    
    @staticmethod           #staticmethod - reprograms the dot so that "self" isn't passed in to let you attach a regular function in a class
    def angle_to_grade(angle):
        'Look-up the percent grade for a given angle in degrees'
        return math.tan(math.radians(angle))*100.0     
    #angle_to_grade = staticmethod (angle_to_grade)
    
    @classmethod
    def from_bbd(cls,bbd):      #classmethod - reprograms the dot so that "cls" is passed in as the first arg, the purpose is to create 
                                #               alternative constructors
        'Construct a circle from a bounding box diagonal'
        radius=bbd/math.sqrt(2.0)/2.0
        return cls(radius)
    
    def get_radius(self):
        return self.diameter/2.0
    
    def set_radius(self, radius):
        self.diameter=radius*2.0
        
        
    #Fairy God Method dotted access automatically convert to method access
    radius=property(get_radius,set_radius)      #transforms attributes access into method access