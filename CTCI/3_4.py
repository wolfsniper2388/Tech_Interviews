''' Hanoi Tower
        Given 3 towers and N disks of different sizes which can slide onto any tower. At the beginning, all the N disks are sorted in ascending order
        of size from top to botttom on tower 1. Write a program to move all the N disks to tower 3 with the following constraints:
        (1) only one disk can be moved at a time
        (2) a disk is slid off the top of one tower onto another tower
        (3) a disk can only be place on top of a larget disk
'''

class Tower:
    def __init__(self, i):
        self.index = i
        self.disks = []
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, index)
    
    def add_disk(self, radius):
        if self.disks and self.disks[-1] <= radius:
            print 'Error add disk of radius %d' %(radius)
        else:
            self.disks.append(radius)

def move_top(orig_tower, dest_tower):
    ''' move the top disk from orig_tower to dest_tower
    '''
    orig_tower_top=orig_tower.disks.pop()
    dest_tower.disks.append(orig_tower_top)
    print "moving Tower %d's top %s to Tower %d" %(orig_tower.index, orig_tower_top, dest_tower.index) 
    
def move_disks(n, orig_tower, dest_tower, aux_tower):
    ''' move n disks from orig_tower to dest_tower using aux_tower as buffer
    '''
    if n<=0:
        return
    move_disks(n-1, orig_tower, aux_tower, dest_tower)
    move_top(orig_tower, dest_tower)
    move_disks(n-1, aux_tower, dest_tower, orig_tower)
    
    
if __name__=='__main__':
    towers=[Tower(i) for i in range(3)]
    n = 4
    # i = n,n-1...,2,1
    for radius in range(n,0,-1):
        towers[0].add_disk(radius)
    print towers[0].disks
    move_disks(n, towers[0], towers[2], towers[1])