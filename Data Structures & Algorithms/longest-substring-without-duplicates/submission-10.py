class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            while (i + longest < len(s)) and (len(s[i:i+longest+1]) == len(set(s[i:i+longest+1]))):
                longest += 1
        
        return longest