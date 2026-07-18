"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return None
            
            nonlocal visited

            if node.val in visited:
                return visited[node.val]

            new_node = Node(node.val)
            visited[node.val] = new_node

            new_neighbors = []

            for i in range(len(node.neighbors)):
                new_neighbors.append(dfs(node.neighbors[i]))

            new_node.neighbors = new_neighbors

            return new_node
        
        return dfs(node)
        

