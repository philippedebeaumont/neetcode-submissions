class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums) + 1
        dp = [[0] * n for _ in range(n)]
        m = float("-inf")

        for i in range(1, len(nums) + 1):
            for j in range(1, len(nums) + 1):
                if j >= i:
                    dp[i][j] = dp[i][j-1] + nums[j-1]
                    m = max(m, dp[i][j])
        return m if len(nums) != 1 else nums[0]
