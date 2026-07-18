class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visiting = set()
        visited = set()

        def has_cycle(node, parent):
            if node in visiting:
                return True
            
            visiting.add(node)
            if adj[node]:
                for neighbor in adj[node]:
                    if neighbor == parent:
                        continue
                    if has_cycle(neighbor, node):
                        return True
            visiting.remove(node)
            visited.add(node)

            return False

        for i in range(n):
            if has_cycle(i, -1):
                return False
        return True