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
        if self.root==None:
            self.root=TreeNode(val)
        else:
            self.add_node_helper(self.root, val)
            
    def add_node_helper(self, node, val):
        if val<node.data:
            #if left subtree is not None, go to right subtree
            if node.left:
                self.add_node_helper(node.left,val)
            #if left subtree is None, then found the place to insert
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
        
    def del_node(self, r, node):
        if not r:
            raise KeyError
        if node.data < r.data:
            r.left = self.del_node(r.left, node)
        elif node.data > r.data:
            r.right = self.del_node(r.right, node)
        # found the node to be deleted, node ==  r now
        else:
            # if it's leaf
            if not r.left and not r.right:
                return None
            # if only has left subtree
            elif not r.left:
                return r.right
            # if only has right subtree
            elif not r.right:
                return r.left
            # if has both left and right subtrees
            else:
                right_min_node = self.find_min(r.right)
                r.data = right_min_node.data
                # del right_min_node will not work because del simply remove the right_min_node's reference, the true object is still there
                r.right = self.del_node(r.right, right_min_node)
        return r
        
    def del_node_with_parent(self,val):
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
    for key in a:
        t.add_node(key)
    r=t.root
    print t.level_order_print(r)
    print t.find_node(r, 3)
    print 'root is ',t.root

    # delete node 40
    print 'New Root: ', t.del_node(r, r.right)
    print 'Test delete, pre order print'
    t.pre_order_print(t.root)
    print '\nTest delete, in order print'
    t.in_order_print(t.root)
    print '\n root is', t.root
    
    
    # delete node 20
    t.del_node_with_parent(20)
    print 'Test delete with parent, pre order print'
    t.pre_order_print(t.root)
    print '\nTest delete with parent, in order print'
    t.in_order_print(t.root)
    print '\n root is', t.root
    
    print 'Testing creating binary search tree using sorted array'
    t=BinarySearchTree()
    t.create_tree(range(1,11))
    print t.root
    t.pre_order_print(t.root)
    print
    t.in_order_print(t.root)