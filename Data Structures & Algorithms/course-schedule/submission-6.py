class graphNode:
    def __init__(self, val):
        self.val = val
        self.prerequisites = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        array = {}

        for p in prerequisites:
            if p[0] not in array:
                array[p[0]] = graphNode(p[0])
            if p[1] not in array:
                array[p[1]] = graphNode(p[1])
            array[p[0]].prerequisites.append(array[p[1]])

        visiting = set()
        visited = set()
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)

            for p in node.prerequisites:
                if not dfs(p):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            
            return True
        
        for c in array.keys():
            if not dfs(array[c]):
                return False
        return True
