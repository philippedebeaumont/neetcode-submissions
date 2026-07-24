class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return float("-inf")
            
            m = (l + r) // 2
            leftSum, leftMax = 0, 0
            for i in range(m - 1, l - 1, -1):
                leftSum += nums[i]
                leftMax = max(leftMax, leftSum)
            
            rightSum, rightMax = 0, 0
            for i in range(m + 1, r + 1):
                rightSum += nums[i]
                rightMax = max(rightMax, rightSum)
            
            return max(dfs(l, m - 1), dfs(m + 1, r), leftMax + nums[m] + rightMax)
        
        return dfs(0, len(nums) - 1)
