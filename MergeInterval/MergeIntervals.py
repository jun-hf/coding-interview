"""
Given a lists of intervals, merge all the 
overlapping intervals to produce a list that has only
mutually exclusive intervals.

Input: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]

Design:

"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def print_interval(self):
        print(f'[{str(self.start)}, {str(self.end)}]')

    def __str__(self):
        return f'{self.start}, {self.end}'
"""
def merge(intervals): take in a list of intervals as a functions
    first check if len less than 2 you can just return the list

    sort all the intervals by the start
    i.e [[2,4], [1, 3]] -> [[1,3], [2,4]]

    initialize a new arr (mergedIntervals) to store the
    merged intervals

    assign the first intervals's start to start
    assign the first intervals's end to end

    
"""
def mergeIntervals(intervals):
    if len(intervals) > 1:
        intervals.sort(key= lambda x: x.start)

        start = intervals[0].start
        end = intervals[0].end
        mergedIntervals = []

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval.start <= end:
                end = max(end, interval.end)
            else:
                mergedIntervals.append(Interval(start, end))
                start = interval.start
                end = interval.end

        mergedIntervals.append(Interval(start, end))

        return mergedIntervals

inter_1 = Interval(2, 8)
inter_2 = Interval(5, 10)
inter_3 = Interval(18, 19)

inter_list = [inter_1, inter_2, inter_3]

a = mergeIntervals(inter_list)

for i in range(len(a)):
    print(a[i])