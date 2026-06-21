class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ")" or c =="]" or c == "}":
                if len(stack) == 0:
                    return False
                x = stack.pop(-1)
                if (x == "(" and c != ")") or (x == "{" and c != "}") or (x == "[" and c != "]"):
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False
