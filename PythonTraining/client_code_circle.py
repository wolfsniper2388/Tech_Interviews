from __future__ import division
# Tutorial
from circle_class import Circle

c=Circle(10)
print 'Tutorial for Circuitous (tm)', Circle.version
print 'a cricle with radius of',c.radius
print 'has an area of', c.area()
print 

from random import random,seed

#Academic Friend
print 'Grant proposal'
print "Using Jenny's number as a seed"
seed(8675309)
n=10
circles=[Circle(random()) for i in range(n)]
average_area=sum([c.area() for c in circles]) / len(circles)
print 'The average area of the %d circles is %.4f'% (n,average_area)


#Rubber Sheet Company
print 'Rubber sheet analytics'
cuts=[0.1,0.2,0.7]
circles=[Circle(r) for r in cuts]
print circles
for c in circles:
    print 'A circle with a cut of', c.radius
    print 'has a perimeter of', c.perimeter()
    print 'and a cold area of', c.area()
    c.radius*=1.1
    # c.set_radius(c.get_radius()*1.1)
    print 'The new cut is',c.radius
    

#National Tire Chain    Learn how to inherit from a class and overload a function
class Tire(Circle):
    'A tire has an odometer corrected perimeter'
    def perimeter(self):
        return Circle.perimeter(self) * 1.25    #use parent class not instance
    __perimeter=perimeter
    
t=Tire(22)
print 'The adjucted radius is',t.radius
print 'The adjusted perimeter is',t.perimeter()
print 'The adjusted area is',t.area()
print


#National Trucking Company    Learn how to use static method
print 'A 5 degree inclinameter reading gives a percent a %.2f%% slope\n' % Circle.angle_to_grade(5)


#National Graphics Company    Learn how to use class method
c=Circle.from_bbd(15)
print 'A circle with a Bounding Box Diagonal of 15'
print 'has a radius of', c.radius
print 'and an area of', c.area()
print 'and a circumference of', c.perimeter()
'''
print 'Class method class Circle:', Circle.from_bbd(15)
print 'Class method class Tire:', Tire.from_bbd(15)
print 'Class method object c:', c.from_bbd(15)
print 'Class method object t:', t.from_bbd(15)
'''


