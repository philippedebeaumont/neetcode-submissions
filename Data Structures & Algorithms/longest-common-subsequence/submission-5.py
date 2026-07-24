class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        current = prev = [0 for j in range(len(text2) + 1)]

        for i in range(1, len(text1) + 1):
            prev = current
            current = [0 for j in range(len(text2) + 1)]
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    current[j] = 1 + prev[j-1]
                else:
                    current[j] = max(current[j-1], prev[j])
        
        return current[-1]
