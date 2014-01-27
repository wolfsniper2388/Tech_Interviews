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
        
        
''' merge all the intervals in intervals
    @param intervals: a list of original intervals to be merged
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
    low = 0
    high = len(orig_intervals)-1
    target = target_interval.start
    while low <= high:
        mid = low+(high-low)/2
        if orig_intervals[mid].start < target:
            low = mid+1
        elif orig_intervals[mid].start > target:
            high = mid-1
        else:
            low = mid
            break
    # after the while loop the position to be inserted in orig_intervals is low
    result_intervals = orig_intervals[:low-1]
    orig_intervals.insert(low, target_interval)
    return result_intervals + merge_intervals(orig_intervals[low-1:])
    
    
if __name__ == '__main__':
    'Q1'
    '''test_cases = [[(1,3),(9,18), (8,10), (2,6)],[(1,1)], [(1,2), (2,3), (2,2)], [(2,6), (1,7)] ]
    for each_test_case in test_cases:
        orig_intervals = [Interval(*each_tuple) for each_tuple in each_test_case]
        print each_test_case, merge_intervals(orig_intervals)'''
    'Q2'
    test_cases = [([(1,2),(3,5),(6,7),(8,10),(12,16)], (4,9)), ([(1,3),(6,9)], (2,5))]
    for each_test_case in test_cases:
        orig_intervals = [Interval(*each_tuple) for each_tuple in each_test_case[0]]
        target_interval = Interval(*each_test_case[1])
        print orig_intervals, target_interval, insert_intervals(orig_intervals, target_interval)
    