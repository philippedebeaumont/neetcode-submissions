class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in pairs:
                if not stack:
                    return False
                
                x = stack.pop()
                
                if pairs[c] != x:
                    return False
            else:
                stack.append(c)
                
        return not stack