class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = max(len(w) for w in wordDict) if wordDict else 0
        
        memo = {}
        
        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for j in range(i, min(len(s), i + t)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)