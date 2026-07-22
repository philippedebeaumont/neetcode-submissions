class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for j in range(n):
            for i in range(m):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j]
                print(dp[i][j])
        
        print(dp)
        return dp[m-1][n-1]