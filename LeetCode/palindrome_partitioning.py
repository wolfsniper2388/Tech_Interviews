''' Q1.
    Given a string s, partition s such that every substring of the partition is a palindrome.
    Return all possible palindrome partitioning of s.
    E.g
        Input: 'bcddeffeh'
        Output: ['dd','ff','effe','b','c','d','e','f','h']
        
    Q2.
    Given a string s, partition s such that every substring of the partition is a palindrome.
    Return the minimum cuts needed for a palindrome partitioning of s.
    E.g.
        Input: 'aab'
        Output: 1, (aa|b)
'''

def is_palindrome(string, string_map):
    if string in string_map:
        return string_map[string]
    start = 0
    end = len(string)-1
    while start < end:
        if string[start] != string[end]:
            string_map[string] = False
            return False
        start += 1
        end -= 1
    string_map[string] = True
    return True


def palindrom_partition_q1(s):
    palindrom_partition_q1_helper(s, {}, [])
    
def palindrome_partition_q1_heler(s,string_map, results):
    