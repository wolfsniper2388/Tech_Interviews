''' Given an array of strings, write a method to group all the anagrams
    E.g.
        input: ['cat','sjtu', 'care', 'utsj', 'just', 'race', 'act', 'tac']
        output: ['cat', 'act', 'tac', 'just', 'sjtu', 'utsj', 'race', 'care']
'''

'''
    Idea: hash the sorted string to a list of anagram strings in the given string list
          e.g    'act' <=> ['cat', 'act', 'tac']
          Then simply retrieve the hashed value in the dict to construct the result
'''



''' 
    @param str_list: the original string list where anagrams will be grouped
    @return a list of strings where anagrams are grouped
'''
def group_anagram(str_list):
    ''' sorted string <=> a list anagrams, e.g.  'jstu' <=> ['sjtu', 'utsj', 'just']
    '''
    str_hash={}
    result_str_list=[]
    for each_str in str_list:
        sorted_str=''.join(sorted(each_str))
        if sorted_str in str_hash:
            str_hash[sorted_str].append(each_str)
        else:
            str_hash[sorted_str]=[each_str]
    
    ''' till now the str_hash will is:
    {'act': ['cat', 'act', 'tac'], 'jstu': ['sjtu', 'utsj', 'just'], 'acer':['care', 'race']}
    Then simply append each string in str_hash[key] to the result 
    '''        
    
    for each_sorted_str in str_hash:
        for each_str in str_hash[each_sorted_str]:
            result_str_list.append(each_str)
    
    return result_str_list

if __name__=='__main__':
    print group_anagram(['cat','sjtu', 'care', 'utsj', 'just', 'race', 'act', 'tac'])
     