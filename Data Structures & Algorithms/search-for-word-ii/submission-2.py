class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
    
    def addWord(self, word, i):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):           
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "#" or board[r][c] not in node.children):
                return
            
            ch = board[r][c]
            child = node.children[ch]
            board[r][c] = "#"
            if child.idx != -1:
                res.append(words[child.idx])
                child.idx = -1
                if not child.children:
                    node.children.pop(ch)
                    board[r][c] = ch
                    return
            
            dfs(r+1, c, child)
            dfs(r-1, c, child)
            dfs(r, c+1, child)
            dfs(r, c-1, child)

            if not child.children and child.idx == -1:
                node.children.pop(ch)

            board[r][c] = ch
                
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res