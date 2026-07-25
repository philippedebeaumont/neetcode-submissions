class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda interval: interval[0])
        prev = float("-inf")
        res = 0

        for i in range(len(intervals)):
            if prev > intervals[i][0]:
                prev = min(prev, intervals[i][1])
                res += 1
            else:
                prev = intervals[i][1]
        
        return res