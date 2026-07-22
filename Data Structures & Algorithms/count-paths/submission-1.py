class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m-1 and j == n-1:
                memo[(i, j)] = 1
                return memo[(i, j)]
            
            if i > m-1 or j > n-1:
                memo[(i, j)] = 0
                return memo[(i, j)]

            memo[(i, j)] = dfs(i+1, j) + dfs(i, j+1)
            return memo[(i, j)]
        
        return dfs(0, 0)