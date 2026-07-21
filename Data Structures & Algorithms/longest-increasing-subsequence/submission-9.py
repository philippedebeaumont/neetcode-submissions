class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(nums):
                return 0
            
            if (i,j) in memo:
                return memo[(i, j)]

            if nums[i] > j:
                memo[(i, j)] = max(1 + dfs(i+1, nums[i]), dfs(i+1, j))
                return memo[(i, j)]
            
            memo[(i, j)] = dfs(i+1, j)
            return memo[(i, j)]
        
        return dfs(0, float("-inf"))