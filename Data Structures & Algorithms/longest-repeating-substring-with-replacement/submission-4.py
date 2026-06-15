from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        frequency = [0] * 26
        max_f = 0

        for r in range(len(s)):
            frequency[ord(s[r]) - ord("A")] += 1
            max_f = max(max_f, frequency[ord(s[r]) - ord("A")])

            if (r - l + 1) - max_f > k:
                frequency[ord(s[l]) - ord("A")] -= 1
                l += 1
        
        return len(s) - l