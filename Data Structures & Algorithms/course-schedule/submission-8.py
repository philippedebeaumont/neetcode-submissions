class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
            
        visiting = set()
        visited = set()
        
        def has_cycle(course):
            if course in visiting:
                return True
            if course in visited:
                return False
                
            visiting.add(course)
            for prereq in adj_list[course]:
                if has_cycle(prereq):
                    return True
            visiting.remove(course)
            visited.add(course)
            return False
            
        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True