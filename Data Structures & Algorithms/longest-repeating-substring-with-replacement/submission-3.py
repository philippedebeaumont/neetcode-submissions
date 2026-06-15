from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        frequency = [0] * 26

        for r in range(len(s)):
            frequency[ord(s[r]) - ord("A")] += 1

            if r - l >= max(frequency) + k:
                frequency[ord(s[l]) - ord("A")] -= 1
                l += 1
            else:
                longest = r - l + 1
        
        return longest