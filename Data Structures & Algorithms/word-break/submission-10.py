class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = current = {}
        for word in wordDict:
            current = root
            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current["#"] = True
        
        memo = {}
        
        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            current = root
            for j in range(i, len(s)):
                if s[j] not in current:
                    break
                current = current[s[j]]
                if "#" in current:
                    if dfs(j+1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)