''' Given a 2D plane with points on it, find a line that passes the most number of points 
'''

from __future__ import division
import sys
import math


class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, (self.x, self.y))

class Line(object):
    round_precision=4      # round to the 4th decimal digit in a float number 
    epsilon=pow(10, -round_precision)
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        if not Line.is_float_equivalent(p1.x, p2.x):
            self.slope = round( (p2.y-p1.y)/(p2.x-p1.x), Line.round_precision)
            self.intercept = round( p2.y- (self.slope)*(p2.x), Line.round_precision)
        else:
            self.slope = sys.float_info.max
            self.intercept = round( p1.x, Line.round_precision)
    
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, (self.p1,self.p2))
              
    
    @staticmethod
    def is_float_equivalent(a,b):
        return abs(a-b) < Line.epsilon  # checks if: abs(a-b)<10^-4

''' insert the new line into hash_table, the mapping is: (slope, intercept) <-> [line1, line2, line3...] (having the same slope and intercept)
'''
def insert_line(new_line, line_hash):
    key = (new_line.slope, new_line.intercept)
    # if the tuple is not in the hash table, then create a new list of lines, add the line into the list and add the key, value to the hash table
    if key not in line_hash:
        lines_list=[]
        lines_list.append(new_line)
        line_hash[key]=lines_list
    # if the tuple already exists, append this new line to the lines_list
    else:
        line_hash[key].append(new_line)


''' count the number of equivalent lines with the keys of 
        (new_line.slope, new_line.intercept)
        (new_line.slope+epsilon, new_line.intercept)
        (new_line.slope-epsilon, new_line.intercept)
    in the line_hash
'''
        
def count_equivalent_lines(line_hash, new_line):
    key0 = (new_line.slope, new_line.intercept)
    count0 = len(line_hash[key0])
    if new_line.slope == sys.float_info.max:
        return count0
    else:
        key1 = (new_line.slope+Line.epsilon, new_line.intercept)
        key2 = (new_line.slope-Line.epsilon, new_line.intercept)
        count1 = 0
        count2 = 0
        if key1 in line_hash:
            count1 = len(line_hash[key1])
        if key2 in line_hash:
            count2 = len(line_hash[key2])
        return count0+count1+count2
    

''' find the line which passes through the most number of points
    @param points: the list of points on the 2D plane 
'''
def find_best_line (points):
    line_hash={}
    n_most_points_pass=0
    best_line=None
    for first_index, first_point in enumerate(points):
        for second_point in points[first_index+1:]:
            new_line = Line(first_point, second_point)
            insert_line(new_line, line_hash)
            n_equivalent_lines=count_equivalent_lines(line_hash, new_line)
            n_points_pass=int( (1+math.sqrt(1+8*n_equivalent_lines))/2 )
            if n_points_pass > n_most_points_pass:
                n_most_points_pass = n_points_pass
                best_line=new_line
    return (best_line, n_most_points_pass)            
    
    

if __name__=='__main__':
    P1=Point(10/3,11)
    P2=Point(10/3,5)
    P3=Point(5/3,6)
    P4=Point(4/3,5)
    P5=Point(-1,0)
    P6=Point(10/3,0)
    points=[P1,P2,P3,P4,P5,P6]
    best_result=find_best_line(points) 
    best_line=best_result[0]
    points_count=best_result[1]
    if best_line.slope == sys.float_info.max:
        print 'the best line is x=%f' %(best_line.intercept)
    else:    
        print 'the best line is y=%fx+%f' %(best_line.slope, best_line.intercept)
    print 'the number of points it passes is', points_count 