''' Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    E.g.
        Input: [100, 4, 200, 1, 3, 2]
        Output : 4 ([1,2,3,4])
'''


''' group the consecutive number together
    @param num_map: number length table, number <=> length of consecutive numbers around number
    @param left: smaller neighbor or self
    @param right: larger neighbor or self
    note: num_map[left]==1 or num_map[right]==1
'''
def merge(num_map, left, right):
    upper_bound = right+num_map[right]-1
    lower_bound = left-num_map[left]+1
    new_len = upper_bound - lower_bound +1
    num_map[upper_bound] = new_len
    num_map[lower_bound] = new_len
    return new_len

def longest_consecutive_seq(A):
    num_map = {}
    max_len = 1
    for num in A:
        if num in num_map:
            continue
        num_map[num] = 1
        if num-1 in num_map:
            max_len = max(max_len, merge(num_map, num-1, num))
        if num+1 in num_map:
            max_len = max(max_len, merge(num_map, num, num+1))
    return max_len


if __name__=='__main__':
    test_cases = [[100, 4, 200, 1, 3, 2], [13,14,2,15,3,17,16,18], [0,3,7,2,5,8,4,6,0,1]]
    for each_test_case in test_cases:
        print each_test_case, longest_consecutive_seq(each_test_case)