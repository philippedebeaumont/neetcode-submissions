class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda interval: interval[0])
        memo = {}

        def dfs(i, limit):
            if (i, limit) in memo:
                return memo[(i, limit)]
            if i == len(intervals):
                memo[(i, limit)] = 0
                return memo[(i, limit)]
            
            if intervals[i][0] < limit:
                memo[(i, limit)] = dfs(i + 1, limit)
                return memo[(i, limit)]
            
            memo[(i, limit)] = max(dfs(i + 1, limit), 1 + dfs(i + 1, intervals[i][1]))
            return memo[(i, limit)]
        
        res = dfs(0, float("-inf"))

        return len(intervals) - res