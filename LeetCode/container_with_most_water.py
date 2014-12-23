''' Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.
    Note: You may not slant the container.

'''
def max_area(height):
    start = 0
    end = len(height)-1
    max_area = -1
    while start < end:
        if height[start] < height[end]:
            max_area = max(max_area, (end-start)*height[start])
            start += 1
        else:
            max_area = max(max_area, (end-start)*height[end])
            end -= 1
    return max_area

if __name__ == '__main__':
    test_cases = [[1,3,7,9,5], [8,19,22,17,6,1]]
    for each_test_case in test_cases:
        print max_area(each_test_case)