''' Given a infinite number of coins of value 5 dollars, 3 dollars and 2 dollors, calculate the number of ways of representing n dollars
'''

''' make_change(10 dollars)  =  make_change(10 dollars, using 0 5 dollars)+
                                make_change(10 dollars, using 1 5 dollars)+
                                make_change(10 dollars, using 2 5 dollars)
                                
                             =  make_change(10 dollars, using 0 5 dollars)+
                                make_change(5 dollars, using 0 5 dollars)+
                                1
    make_change(10 dollars, using 0 5 dollars) = make_change(10 dollars, using 0 5 dollars, 0 3 dollars)+
                                                 make_change(10 dollars, using 0 5 dollars, 1 3 dollars)+
                                                 make_change(10 dollars, using 0 5 dollars, 2 3 dollars)+
                                                 make_change(10 dollars, using 0 5 dollars, 3 3 dollars)
    
   make_change(5 dollars, using 0 5 dollars) =   make_change(5 dollars, using 0 5 dollars, 0 3 dollars)+
                                                 make_change(10 dollars, using 0 5 dollars, 1 3 dollars)+
                           
'''

def make_change(n, values):
    values_dict={}
    for i in range(len(values)-1):
        values_dict[values[i]]=values[i+1]
    values_dict[values[-1]]=values[-1]
    
    # values_dict = {5:3, 3:2, 2:2}
    return make_change_helper(n, values[0], values_dict)


def make_change_helper(n, denom, values_dict):
    next_denom=values_dict[denom]
    # next_denom == denom <=> next_denom is the last element in values, i.e. 2 here
    if next_denom == denom:
        # the n can be divided by next_denom, this is one valid way
        if n % next_denom ==0:
            return 1
        else:
            return 0
    
    ways=i=0
    while i*denom <=n:
        ways+=make_change_helper(n-i*denom, next_denom, values_dict)
        i+=1 
    return ways
         
        
if __name__=='__main__':
    print make_change(10,[5,3,2])