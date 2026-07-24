class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j, count):
            if (i, j, count) in memo:
                return memo[(i, j, count)]
            
            if i >= len(text1) or j >= len(text2):
                memo[(i, j, count)] = count
                return memo[(i, j, count)]

            if text1[i] == text2[j]:
                memo[(i, j, count)] = dfs(i+1, j+1, count+1)
                return memo[(i, j, count)]
            
            memo[(i, j, count)] = max(dfs(i+1, j, count), dfs(i, j+1, count))
            return memo[(i, j, count)]

        return dfs(0, 0, 0)
        