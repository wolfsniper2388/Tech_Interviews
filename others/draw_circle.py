''' Pure storage:
    Given a parameter r2, where the equation x^2+y^2=r2 holds.
    Return a list of points that 
        (1) x and y are both integers
        (2) fits the circle equation
'''

from sets import Set

import profile



def draw_circle(r2):
    result = Set([])
    x = 1
    y = 0
    while x*x <= r2:
        for y in range(x+1):
            if x*x+y*y == r2:
                result.update(Set([(x,y),(x,-y),(-x,-y),(-x,y),(y,x),(y,-x),(-y,-x),(-y,x)]))
        x+=1
    return result

def draw_circle_bi_search(r2):
    result = Set([])
    x = 1
    y = 0
    while x*x <= r2:
        y_start = 0
        y_end = x
        while y_start <= y_end:
            y_mid = y_start+(y_end-y_start)/2
            if x*x + y_mid*y_mid == r2:
                result.update(Set([(x,y_mid),(x,-y_mid),(-x,-y_mid),(-x,y_mid),(y_mid,x),(y_mid,-x),(-y_mid,-x),(-y_mid,x)]))
                break
            elif x*x + y_mid*y_mid < r2:
                y_start = y_mid+1
            else:
                y_end = y_mid-1
                
                 
        x+=1
    return result

if __name__=='__main__':
    profile.run('print draw_circle(1000000)')
    profile.run('print draw_circle_bi_search(1000000)')
    
        