class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        step_1, step_2 = 1, 1

        for i in range(1, len(s)):
            current = 0

            if s[i] != "0":
                current += step_1
            
            two_digits = int(s[i-1:i+1])
            if 10 <= two_digits <= 26:
                current += step_2

            if current == 0:
                return 0
            
            step_1, step_2 = current, step_1
        
        return step_1