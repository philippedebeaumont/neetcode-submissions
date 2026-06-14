class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        unique = set()
        longest = 0

        while r <= len(s)-1:
            if s[r] not in unique:
                unique.add(s[r])
                r += 1
                longest = max(longest, r-l)
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
                unique.add(s[r])
                r += 1
                longest = max(longest, r-l)
            
        return longest


            
