class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfWord = True
    
    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endOfWord
    
    def startwith(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        memo = {}
        
        def dfs(i):
            if i == len(s):
                memo[i] = True
                return True

            if i in memo:
                return memo[i]
            
            for j in range(i, len(s)):
                if trie.search(s[i : j+1]):
                    if dfs(j+1):
                        return True

            memo[i] = False
            return False

        return dfs(0)