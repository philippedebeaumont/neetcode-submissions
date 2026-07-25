class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        l, r = 0, len(intervals) - 1

        while l <= r:
            m = (l + r) // 2

            if intervals[m][0] < newInterval[0]:
                l = m + 1
            else:
                r = m - 1
        
        intervals.insert(l, newInterval)

        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res