'''
https://www.quora.com/challenges#ontology
'''

from collections import deque
from copy import deepcopy

class RadixNode():
    def __init__(self, val):
        self.val = val
        self.n_subpaths = 0
        self.children = []
    
class RadixTree():
    def __init__(self):
        self.root = RadixNode("")
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.val)
    
    def deserialize(self, sentences):
        sentences_list = [each_sentence.split() for each_sentence in sentences]
        for each_sentence_list in sentences_list:
            self.insert(each_sentence_list)
        self.updateSubpathsNum(self.root)
    
    def insert(self, words):
        curr_node = self.root
        for word in words:
            values = [child.val for child in curr_node.children]
            if word in values:
                idx = values.index(word)
                curr_node = curr_node.children[idx]
                continue
            new_node = RadixNode(word)
            curr_node.children.append(new_node)
            curr_node = new_node
            
    def updateSubpathsNum(self, node):
        if node.children == []:
            node.n_subpaths = 1
            return node.n_subpaths
        for child in node.children:
            node.n_subpaths += self.updateSubpathsNum(child)
        return node.n_subpaths
    
    def serialize(self):
        'Convert radix tree back to a list of strings'
        def serialize_helper(self, node):
            if node.children == []:
                return [[node.val]]
            results = []
            for i in range(len(node.children)):
                results.extend(self.serialize_helper(node.children[i]))
        
            for result in results:
                result.append(node.val)
                return deepcopy(results)
    
        results = serialize_helper(self.root)
        paths= []
        for result in results:
            result.pop()
            paths.append(' '.join(reversed(result)))
        return paths
            
    def matchNum(self, query_words):
        '''
        return the number of query prefix matches
        '''
        matches = 0
        curr_node = self.root
        n_words = len(query_words)
        for i in range(n_words-1):
            children_values = [child.val for child in curr_node.children]
            
            if query_words[i] not in children_values:
                return 0
            else:
                idx = children_values.index(query_words[i])
                curr_node = curr_node.children[idx]
                   
        children_values = [child.val for child in curr_node.children]
        last_word = query_words[-1]
        for i,each_child_value in enumerate(children_values):
            if each_child_value.startswith(last_word):
                matches += curr_node.children[i].n_subpaths
        return matches

class OntologyNode():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.questions = []
        self.radix_tree = None
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.name)

class OntologyTree():
    def __init__(self):
        self.root = OntologyNode("")
        self.node_map = {}  # node name <=> node
        
    def deserialize(self, input_str):
        input = input_str.split()
        if not input:
            return
        node = OntologyNode(input[0])
        self.root = node
        self.node_map[node.name] = node
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
                    node.parent = parentStack[-1]
                    self.node_map[node.name] = node
                    
            else:
                # deal with ')'
                parentStack.pop()
    
    def add_question(self, q):
        tmp = q.split(": ")
        topic = tmp[0]
        question = tmp[1]
        curr_node = self.node_map[topic]
        if not curr_node:
            return
        curr_node.questions.append(question)
        parent_node = curr_node.parent
        while parent_node:
            parent_node.questions.append(question)
            parent_node = parent_node.parent
    
    def build_radix_tree(self):
        visited = set()
        def build_radix_tree_helper(node, visited):
            #print node
            node.radix_tree = RadixTree()
            node.radix_tree.deserialize(node.questions)
            #node.radix_tree.dfsPrintSubpathsNum()
            visited.add(node)
            for child in node.children:
                if child not in visited:
                    build_radix_tree_helper(child,visited)
        
        build_radix_tree_helper(self.root, visited)
        
    def get_query_match(self, q):
        tmp = q.split()
        topic = tmp[0]
        query = tmp[1:]
        curr_node = self.node_map[topic]
        return curr_node.radix_tree.matchNum(query)
    
    
if __name__ == '__main__':
    tquestions = []
    tqueries = []    
    N = int(raw_input())
    ontology = str(raw_input())
    M = int(raw_input())
    for i in xrange(M):
        tquestion = str(raw_input())
        tquestions.append(tquestion)
    K = int(raw_input())
    for i in xrange(K):
        tquery = str(raw_input())
        tqueries.append(tquery)

    ot = OntologyTree()
    ot.deserialize(ontology)
    
    for tquestion in tquestions:
        ot.add_question(tquestion)
    
    ot.build_radix_tree()
    for tquery in tqueries:
        print ot.get_query_match(tquery)