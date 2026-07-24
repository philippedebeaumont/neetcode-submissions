class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        current = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = current.copy()
            
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    current[j] = 1 + prev[j - 1]
                else:
                    current[j] = max(current[j - 1], prev[j])

        return current[n]
