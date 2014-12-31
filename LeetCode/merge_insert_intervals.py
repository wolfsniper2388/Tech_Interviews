''' Q1.
    Given a collection of intervals, merge all overlapping intervals.
    Input: [1,3],[2,6],[8,10],[15,18]
    Ouput: [1,6], [8,10], [15,18]
    
    Q2.
    Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
    You may assume that the intervals were initially sorted according to their start times.
    Input: ([[1,3],[6,9]], [2,5])
    Output: [[1,5], [6,9]]
    Input: ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9])
    Output: [[1,2], [3,10], [12,16]]
    
'''
class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, (self.start, self.end))
    def __lt__(self, other):
        return self.start<other.start
        
        
''' merge all the intervals in orig_intervals
    refer to CTCI 1_5
    @param orig_intervals: a list of original intervals to be merged
    @return: a list of intervals that has been merged 
'''
def merge_intervals(orig_intervals):
    orig_intervals = sorted(orig_intervals)
    result_intervals = []
    prev_interval = orig_intervals[0]
    for curr_interval in orig_intervals[1:]:
        if curr_interval.start <= prev_interval.end:
            new_interval = Interval(prev_interval.start, max(curr_interval.end, prev_interval.end))
            prev_interval = new_interval
        else:
            result_intervals.append(prev_interval)
            prev_interval = curr_interval
    result_intervals.append(prev_interval)
    return result_intervals


''' insert the target_interval to orig_intervals
    Algorithm: use binary search to find the position to insert
    and then merge intervals
    @param orig_intervals: a list of original intervals
    @param target_interval: the interval to be inserted to orig_intervals
    @return: a list of result intervals where target_interval has been inserted 
'''
def insert_intervals(orig_intervals, target_interval):
    result = []
    if not orig_intervals:
        result.append(target_interval)
        return result
    for i, curr_interval in enumerate(orig_intervals):
        if curr_interval.end < target_interval.start:
            result.append(curr_interval)
        elif curr_interval.start > target_interval.end:
            result.append(target_interval)
            break
        else:
            target_interval = Interval(min(curr_interval.start, target_interval.start), max(curr_interval.end, target_interval.end))
    # if i is already at end, append the target_interval and return
    if i == len(orig_intervals):
        result.append(target_interval)
        return result
    # else append everything else after index i , and return
    result.extend(orig_intervals[i:])
    return result
    
    
if __name__ == '__main__':
    'Q1'
    print 'Q1'
    test_cases = [[(1,3),(9,18), (8,10), (2,6)],[(1,1)], [(1,2), (2,3), (2,2)], [(2,6), (1,7)] ]
    for each_test_case in test_cases:
        orig_intervals = [Interval(*each_tuple) for each_tuple in each_test_case]
        print each_test_case, merge_intervals(orig_intervals)
    'Q2'
    print 'Q2'
    test_cases = [([(1,2),(3,5),(6,7),(8,10),(12,16)], (4,9)), ([(1,3),(6,9)], (2,5)), ([],[2,7]), ([(1,5)], (2,3))]
    for each_test_case in test_cases:
        orig_intervals = [Interval(*each_tuple) for each_tuple in each_test_case[0]]
        target_interval = Interval(*each_test_case[1])
        print orig_intervals, target_interval, insert_intervals(orig_intervals, target_interval)
    