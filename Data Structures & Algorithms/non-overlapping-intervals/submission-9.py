class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals = sorted(intervals, key = lambda interval: interval[0])
        dp = [1] * n

        for i in range(1, n):
            for j in range(n):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return n - max(dp)