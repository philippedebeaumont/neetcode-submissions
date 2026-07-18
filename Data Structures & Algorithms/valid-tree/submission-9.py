class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parents = list(range(n))
        self.Size = [1] * n
    
    def find(self, node):
        if self.Parents[node] != node:
            self.Parents[node] = self.find(self.Parents[node])
        return self.Parents[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.comps -= 1
        if self.Size[pu] >= self.Size[pv]:
            self.Parents[pv] = pu
            self.Size[pu] = self.Size[pu] + self.Size[pv]
        else:
            self.Parents[pu] = pv
            self.Size[pv] = self.Size[pu] + self.Size[pv]
        
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return True if dsu.components() == 1 else False
        