'''	Implement Binary search tree: create tree, add node, find node, delete node
'''
from BinaryTree import BinaryTree, TreeNode

class BinarySearchTree(BinaryTree):
    def create_tree(self,seq):
        self.root=self.create_tree_helper(seq)
        
    def create_tree_helper(self,seq):
        if not seq:
            return None
        mid=(len(seq)-1)/2
        n=TreeNode(seq[mid])
        n.left=self.create_tree_helper(seq[:mid])
        n.right=self.create_tree_helper(seq[mid+1:])
        return n
    
    def add_node(self, val):
        ''' The reason to use helper function here is that we want to set the root and 
            don't want this operation to be in the recursion.
            So pull out all the operations that we don't want to be in the recursion, and then
            call the recursion function which is a helper function here
            
            Another reason to use helper function is that user may have no access to the 
            private data like root here, so when they make the call they cannot pass in root as 
            a parameter, however the function call must use root as a parameter. In this situation,
            we can have a interface function which takes the user's parameter and call the helper function inside
            the interface function to pass the private data as parameters. E.g, the add_node(val) is a interface
            function which takes the parameter 'val' from user, but to implement add_node, we must know
            the root of the tree, so call add_node_helper function to actually pass the root parameter
        '''
        if self.root==None:
            self.root=TreeNode(val)
        else:
            self.add_node_helper(self.root, val)
            
    def add_node_helper(self, node, val):
        if val<node.data:
            #if right subtree is not None, go to right subtree
            if node.left:
                self.add_node_helper(node.left,val)
            #if right subtree is None, then found the place to insert
            else:
                new_node=TreeNode(val)
                node.left=new_node
                new_node.parent=node
        elif val>node.data:
            #if right subtree is not None, go to right subtree
            if node.right:  
                self.add_node_helper(node.right,val)
            #if right subtree is None, then found the place to insert
            else:
                new_node=TreeNode(val)
                node.right=new_node
                new_node.parent=node
        else:
            print 'Found same value, please check the input!'
            raise IndexError(val)
    
    def find_node(self, node, val):
        if node==None:
            return None
        if val<node.data:
            return self.find_node(node.left,val)
        elif val>node.data:
            return self.find_node(node.right, val)
        else:
            return node
    # !!!!! Very Important !!!!!!
    def del_node(self,node,val):
        # delete the root and root has only left/right subtree
        if node==self.root and not node.left:
            self.root=node.right
            del node
            return self.root    
        elif node==self.root and not node.right:
            self.root=node.left
            del node
            return self.root
    
    
        if node==None:
            print 'Element not found'
        elif val<node.data:
            node.left=self.del_node(node.left, val)     #whatever happened down there, just give me the root of my left subtree
        elif val>node.data:
            node.right=self.del_node(node.right, val)       #whatever happened down there, just give me the root of my right subtree
        # val==node.data, found the node to be deleted
        elif node.right and node.left:
            min_node=self.find_min(node.right)      #find the node with min data in the right subtree
            node.data=min_node.data
            node.right=self.del_node(node.right, min_node.data)     #whatever happened down there, just give me the root of my right subtree
        else:
            # left subtree is None
            if not node.left:
                tmp_node=node
                node=node.right     #the root of the left/right subtree of my parent is my right child
                del tmp_node
            # right subtree is None
            elif not node.right:
                tmp_node=node
                node=node.left      #the root of the left/right subtree of my parent is my left child
                del tmp_node
        return node
        
    def del_nodeNR(self,val):
        node=self.find_node(self.root,val)
        if node==None:
            print 'did not find the node with data of ',val
        else:
            self.del_node_helper(node,val)
        
    def del_node_helper(self,node,val):
        # node has both left and right subtree
        if node.right and node.left:
            min_node=self.find_min(node.right)
            node.data=min_node.data
            self.del_min(min_node)   
        # node only has right subtree, pull the right child up, like 73 
        elif node.right and not node.left:
            if node==self.root:
                self.root=node.right
            else:
                if node==node.parent.left:
                    node.parent.left=node.right
                else:
                    node.parent.right=node.right
            del node
        # node only has left subtree, pull the left child up, like 7    
        elif node.left and not node.right:
            if node==self.root:
                self.root=node.left
            else:
                if node==node.parent.left:
                    node.parent.left=node.left
                else:
                    node.parent.right=node.left
            del node
        # node is a leaf    
        else:
            del node
            
    def find_min(self,node):
        while node.left:
            node=node.left
        return node
    
    def del_min(self,min_node):
        # don't forget min_node's right subtree
        if min_node==min_node.parent.left:
            min_node.parent.left=min_node.right
        else:
            min_node.parent.right=min_node.right        
        del min_node     
         
         
        

if __name__=='__main__':
    t=BinarySearchTree()
    ''' The tree is :
                        20
                     /      \
                  10          40
                /    \       /  \
               3       17   35    73
              /  \     / \          \
             1    7  15  18         89
             \    /  /
              2  5  11
                / \   \
               4   6   12
    
    '''
    a=[20,10,40,3,17,35,73,1,7,15,18,89,2,5,11,4,6,12]
    b=[20,30,40]
    for key in a:
        t.add_node(key)
    r=t.root
    t.level_order_print(r)
    print t.find_node(r, 3)
    print 'root is ',t.root
    '''
    t.del_nodeNR(10)
    print 'Test delete NR, pre order print'
    t.pre_order_print(r)
    print '\nTest delete NR, in order print'
    t.in_order_print(r)
    print '\n root is', t.root
    '''
    t.del_node(r,73)
    print 'Test delete, pre order print'
    t.pre_order_print(t.root)
    print '\nTest delete, in order print'
    t.in_order_print(t.root)
    print '\n root is', t.root
    
    print 'Testing creating tree with recursion CTCI 4_3'
    t=BinarySearchTree()
    t.create_tree(range(1,11))
    print t.root
    t.pre_order_print(t.root)
    print
    t.in_order_print(t.root)