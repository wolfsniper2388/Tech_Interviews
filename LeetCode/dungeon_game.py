'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 2D grid. 
Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. 
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; 
other rooms are either empty (0's) or contain magic herbs that increase the knight's health (positive integers).
In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)    -3     3
-5        -10    1
10        30     -5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

'''


''' Using a 2D dynamic programming
    min_health [i][j] = (min_health [i+1][j], min_health[i][j+1]) - dungeon[i][j] if the result is > 0 else 1
'''
def min_health_dungeon_1(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])
    min_health = [[1 for j in range(n)] for i in range(m)]
    ''' initialize min_health[m-1][n-1], if the last cell costs x health, that means the knight needs at least x health to enter this cell
        if the last cell is herb, we simply say the knight doesn't need health (or need 0 health to enter this cell)
    '''
    min_health[m-1][n-1] = 1-dungeon[m-1][n-1] if dungeon[m-1][n-1] < 0 else 1
    for j in range(n-2, -1, -1):
        tmp = min_health[m-1][j+1] - dungeon[m-1][j]
        min_health[m-1][j] = tmp if tmp > 0 else 1
    for i in range(m-2, -1, -1):
        tmp = min_health[i+1][n-1] - dungeon[i][n-1]
        min_health[i][n-1] = tmp if tmp > 0 else 1
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            tmp = min(min_health[i+1][j], min_health[i][j+1]) - dungeon[i][j]
            min_health[i][j] = tmp if tmp > 0 else 1
    return min_health[0][0]

def min_health_dungeon_2(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])
    min_health = [1] * n
    min_health[n-1] = 1-dungeon[m-1][n-1] if dungeon[m-1][n-1] < 0 else 1
    for j in range(n-2, -1, -1):
        tmp = min_health[j+1] - dungeon[m-1][j]
        min_health[j] = tmp if tmp > 0 else 1
    for i in range(m-2, -1, -1):
        tmp = min_health[n-1] - dungeon[i][n-1]
        min_health[n-1] = tmp if tmp > 0 else 1
        for j in range(n-2, -1, -1):
            tmp = min(min_health[j], min_health[j+1]) - dungeon[i][j]
            min_health[j] = tmp if tmp > 0 else 1
    return min_health[0]


if __name__=='__main__':
    dungeon = [[-2, -5, -4],
               [-1,  1, -3],
               [-2,  2, -6]]
    print min_health_dungeon_1(dungeon)
    print min_health_dungeon_2(dungeon)
        
    
    
    