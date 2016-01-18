'''
Implementation of radix tree

'''
from copy import deepcopy

class RadixNode():
    def __init__(self, val):
        self.val = val
        self.n_subpaths = 0
        self.children = []
    
class RadixTree():
    def __init__(self):
        self.root = RadixNode("")
    
    def deserialize(self, sentences):
        sentences_list = [each_sentence.split() for each_sentence in sentences]
        print sentences_list
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
            #curr_node = curr_node.children[-1]
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
        results = self.serialize_helper(self.root)
        paths= []
        for result in results:
            result.pop()
            paths.append(' '.join(reversed(result)))
        return paths
            
    def serialize_helper(self, node):
        if node.children == []:
            return [[node.val]]
        results = []
        for i in range(len(node.children)):
            results.extend(self.serialize_helper(node.children[i]))
        
        for result in results:
            result.append(node.val)
        return deepcopy(results)
    
    def dfsPrintSubpathsNum(self):
        visited = set()
        self.dfsPrintSubpathsNum_helper(self.root, visited)
    
    def dfsPrintSubpathsNum_helper(self, node, visited):
        print node.val,":", node.n_subpaths
        visited.add(node)
        for child in node.children:
            if child not in visited:
                self.dfsPrintSubpathsNum_helper(child, visited)
        
    
    def matchNum(self, query):
        '''
        return the number of query prefix matches
        '''
        query_words = query.split()
        if not query_words:
            return 0
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
        

if __name__=='__main__':
    #questions = [['how','do','birds','fly'],['how','endangered','are','eagles'],['what','do','eagles','eat']]
    questions = ['how are you doing', 'how are we doing','how are we eating', 'what do eagles eat']
    rt = RadixTree()
    rt.deserialize(questions)
    #rt.dfsPrintSubpathsNum()
    print rt.serialize()
    print rt.matchNum('how are wed')
