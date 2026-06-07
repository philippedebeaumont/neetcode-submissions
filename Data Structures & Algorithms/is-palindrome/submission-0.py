class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            if not (("a" <= s[l] <= "z") or ("A" <= s[l] <= "Z") or ("0" <= s[l] <= "9")):
                l += 1
            elif not (("a" <= s[r] <= "z") or ("A" <= s[r] <= "Z") or ("0" <= s[r] <= "9")):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True