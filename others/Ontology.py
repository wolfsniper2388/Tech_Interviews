'''
https://www.quora.com/challenges#ontology
'''

from collections import deque
class Parser():
    pass

class OntologyNode():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.questions = []
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.name)

class OntologyTree():
    def __init__(self):
        self.root = OntologyNode("")
        
    def deserialize(self, input_str):
        input = input_str.split()
        if not input:
            return
        node = OntologyNode(input[0])
        self.root = node
        parentStack = [node]
        hasChild = False
        for item in input[1:]:
            if item != ')':
                if item == '(':
                    # deal with '(' push previous node to parentStack
                    parentStack.append(node)
                else:
                    # deal with a word
                    node = OntologyNode(item)
                    parentStack[-1].children.append(node)
                    
            else:
                # deal with ')'
                parentStack.pop()
    
    def levelOrder(self, r):
        all_levels = []
        curr_level_TreeNodes = []
        TreeNode_q = deque([])
        n_curr_level_TreeNodes = 1
        n_next_level_TreeNodes = 0
        TreeNode_q.append(r)
        while TreeNode_q:
            curr_TreeNode = TreeNode_q.popleft()
            n_curr_level_TreeNodes -= 1
            curr_level_TreeNodes.append(curr_TreeNode.name)
            for child in curr_TreeNode.children:
                if child:
                    TreeNode_q.append(child)
                    n_next_level_TreeNodes += 1
            if n_curr_level_TreeNodes == 0:
                all_levels.append(curr_level_TreeNodes)
                curr_level_TreeNodes = []
                n_curr_level_TreeNodes = n_next_level_TreeNodes
                n_next_level_TreeNodes = 0
        return all_levels

if __name__ == '__main__':
    ontology = 'Animals ( Reptiles ( Snake ) Birds ( Crows Eagles ) )'
    ot = OntologyTree()
    ot.deserialize(ontology)
    print ot.levelOrder(ot.root)