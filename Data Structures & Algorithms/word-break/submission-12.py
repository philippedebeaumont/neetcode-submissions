class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = {}
        for word in wordDict:
            current = root
            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current['#'] = True

        t = max(len(w) for w in wordDict) if wordDict else 0

        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            current = root
            for j in range(i, min(len(s), i+t)):
                char = s[j]
                if char not in current:
                    break
                
                current = current[char]
                
                if '#' in current:
                    if dfs(j + 1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)