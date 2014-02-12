''' There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
    You begin the journey with an empty tank at one of the gas stations.
    Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
    E.g. 
        Input: gas = [7,5,3,2], cost = [5,4,3,5]
        Output: 0
'''

def gas_station_1(gas, cost):
    if len(gas) != len(cost):
        return -1
    n = len(gas)
    for start in range(n):
        if dfs(start, [0], 0, n, gas, cost):
            return start 
    return -1

def dfs(i, curr_gas, curr_nodes_visited, n, gas, cost):
    if curr_nodes_visited == n:
        return True
    curr_gas[0] = curr_gas[0] + gas[i] - cost[i]
    if curr_gas[0] < 0:
        return False
    return dfs((i+1)%n, curr_gas, curr_nodes_visited+1, n, gas, cost)

''' 
    We have two questions:
        1. Can I travel around?
        2.  if yes where is the start point
    define diff[i] = gas[i]-cost[i]
    then if sigma i=0->n diff[i] >=0 then we can travel around, q1 is simple
    now consider q2
    if we have a range on the circle, say [i,j], j>i
    if sum[i,j] = sigma k=i->j diff[k] < 0 then we know the start point can never be in this range
    suppose i is the start point of [0..n], we can infer that:
    sum[k,i-1]<0 for any 0<=k<i-1, otherwise, k will be the solution
    so for q2, we simply try to find the first j, so that sum[0,j]<0, if no such j exists, 0 is the solution
'''
def gas_station_2(gas, cost):
    sum=total=0
    start_node=-1
    for i in range(len(gas)):
        sum+=gas[i]-cost[i]
        total+=gas[i]-cost[i]
        if sum<0:
            start_node = i
            sum = 0
    return start_node+1 if total>=0 else -1
    
if __name__=='__main__':
    test_cases = [([5,3,2,7],[4,3,5,5])]
    for each_test_case in test_cases:
        gas,cost = each_test_case
        print gas, cost, gas_station_1(gas, cost),gas_station_2(gas, cost)