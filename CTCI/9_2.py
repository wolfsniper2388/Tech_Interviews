''' 1. how many possible paths are there for a robot to go from (0,0) to (X,Y)
    while the robot can only move down or right
    assume the upper left coordinate is (0,0), downward is x axis, rightward is y axis
    
    2. print all the possible paths that the robot can go from (0,0) to (X,Y) if there are 
    some off-limits points that the robot cannot step on
'''

from copy import deepcopy

cache={}
''' The number of possible ways for the robot go to (x,y)
'''
def robot_way(x,y):
    if x<0 or y<0:
        return 0
    if x==0 and y==0:
        return 1
    if y == 0 or x == 0:
        return 1
    if (x,y) in cache:
        return cache[(x,y)]
    
    cache[(x,y)]=robot_way(x,y-1)+robot_way(x-1,y)
    return cache[(x,y)]

'''
    find all the paths the robot can go from (0,0) to (x,y)
    @return: [[(0,0), (0,1), (1,1)], [path2], [path3], [path4],... ], a list of paths, each path is a list of points on the path
    
'''
paths={}
def find_paths(x, y, landmines):
    if (x,y) in landmines:
        return []
    if x==0 and y==0:
        return [[(0,0)]]
 
    if (x,y) in paths:
        return paths[(x,y)]
    from_up_path=[]     # all the paths to (x-1,y)
    from_left_path=[]   # all the paths to (x,y-1)
    if x!=0 and (x-1,y) not in landmines:
        from_up_path=deepcopy(find_paths(x-1,y,landmines))
        for each_path in from_up_path:
            each_path.append((x,y))
    if y!=0 and (x,y-1) not in landmines:
        from_left_path=deepcopy(find_paths(x,y-1,landmines))
        for each_path in from_left_path:
            each_path.append((x,y))
    paths[(x,y)]=from_up_path+from_left_path
    return paths[(x,y)]


if __name__=='__main__':
    print robot_way(4,3)
    
    off_limits=[(1,2),(0,1)]
    paths=find_paths(3,4,off_limits)
    print 'there are %d paths' %(len(paths))
    for each_path in paths:
        print each_path