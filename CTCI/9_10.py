''' Given a bunch of boxes, each with width wi, height hi and depth di. The boxes cannot be rotated and only can be stacked on top of one another 
    if each box is strictly larger than the box above it in width, height and depth.
    Implement a method to build the tallest stack possible (find the biggest height). The height of a stack is the sum of all the heights of boxes
'''

class Box(object):
    def __init__(self, height, width, depth):
        self.height=height
        self.width=width
        self.depth=depth
    
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, (self.height, self.width, self.depth))
    
    ''' can box be above self
        @param box: another box
        @return: true if self's height, width and depth are all smaller than the box
                 false if else
    '''
    def can_be_above (self, box):
        if self.height < box.height and self.width < box.width and self.depth < box.width:
            return True
        else:
            return False

''' 
    @param box_stack: a list of boxes
    @return: the sum of height of all the boxes in the stack  
'''
def get_stack_height(box_stack):
    stack_height=0
    for box in box_stack:
        stack_height+=box.height
    return stack_height


        
''' create a box stack out of boxes, using bottom_box as bottom
    @param boxes: a list of box 
    @param bottom_box: bottom box in stack  
    @param stack_map: box <=> box stack based on the box with the maximum height
                     e.g b1 <=> [b1, b3, b2, b5] means stack [b1, b3, b2, b5] is the tallest stack possible based on b1                                                                                           
    @return: the stack with maximum height based on box  
'''
def create_stack(boxes, bottom_box, stack_map):
    if bottom_box and bottom_box in stack_map:
        return stack_map[bottom_box]
    
    max_height=0
    max_stack=[]
    
    for box in boxes:
        # if box can be above the bottom box, then create a new stack, using box as the bottom box
        if box.can_be_above(bottom_box):
            new_stack=create_stack(boxes, box, stack_map)
            new_height=get_stack_height(new_stack)
            # if new_height is larger, then update max_height and max_stack
            if new_height > max_height:
                max_height = new_height
                max_stack = new_stack
    
    # insert bottom_box at the beginning of max_stack
    max_stack.insert(0, bottom_box)
    stack_map[bottom_box]=max_stack
    return max_stack

def get_max_stack_height(boxes):
    max_height=0
    max_stack=[]
    stack_map={}
    for each_bottom_box in boxes:
        curr_stack=create_stack(boxes, each_bottom_box, stack_map)
        curr_height=get_stack_height(curr_stack)
        if curr_height > max_height:
            max_stack=curr_stack
            max_height = curr_height
    return (max_height,max_stack)


if __name__=='__main__':
    b1=Box(5,5,5)
    b2=Box(5,4,4)
    b3=Box(3,3,4)
    b4=Box(2,2,2)
    b5=Box(1,1,2)
    boxes=[b1,b2,b3,b4,b5]
    
    height_stack_tuple=get_max_stack_height(boxes)
    print 'The max stack is', height_stack_tuple[1]
    print 'Its height is', height_stack_tuple[0]
    