''' Given n items: z1, z2... zn, where zi has a value vi and weight wi, the maximum weight we can carry is W
    maximize the sum of the values in the knapsack so that the sum of weights must be less than W
    i.e maximize sigma i=0->n (vixi), subject to sigma i=0->n (wixi), where xi = {0,1} 
'''

''' using dynamic programming
    for 0-1 knapsack problem
    suppose m[i,w] is the maximum total values that can be attained
     with total weight less than w and items up to i
    then m[n, W] is what we want
    m[0, w]=0
    m[i,w] = m[i-1. w] if wi>w (the new item's weight exceeds the current limit)
    m[i,w] = max(m[i-1, w], vi+m[i-1. w-wi]) (m[i-1, w] means not select i, vi+m[w-wi] means select i)
    
    
    for unbounded knapsack problem
    i.e maximize sigma i=0->n (vixi), subject to sigma i=0->n (wixi), where xi = {0,1,2,3,...} 
        which means the same item can be selected multiple times  
    suppose m[w] is the maximum total values that can be attained
     with total weight less than w
    m[0] = 0
    m[w] = max(vi+ m[w-wi]), where wi<=w
'''



cache={}

def zero_one_knapsack(items, capacity):
    
    
    ''' return the max total value can be attained with total weight less than w up to the first i itmes (0-based) 
    '''
    def best_value(i, w):
        if i==-1:
            return 0
        if (i,w) in cache:
            return cache[(i,w)]
        weight,value = items[i]
        if weight > w:
            cache[(i,w)]=best_value(i-1,w)
        else:
            cache[(i,w)]=max(best_value(i-1, w), best_value(i-1, w-weight)+value)
        return cache[(i,w)]
    
    n = len(items)
    selected=[]    
    w=capacity
    for i in xrange(n-1, -1, -1):
        # adding items[i] would make difference, add items[i] to selected
        if best_value(i, w) != best_value(i-1, w):
            selected.append(items[i])
            w -= items[i][0]
    return best_value(n-1, capacity), selected


if __name__=='__main__':
    #weights=[2,5,1,10,7,19,25]
    #values= [3,7,1,15,8,2,28]
    weights=[23,31,29,44,53,38,63,85,89,82]
    values=[92,57,49,68,60,43,67,84,87,72]
    items=zip(weights, values)
    capacity=165
    print zero_one_knapsack(items, capacity)
    