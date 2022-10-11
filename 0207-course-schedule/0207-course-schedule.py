class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preMap[course].append(pre)
            
        # preMap ready
        
        
        visited = set()
        # to keep track if there are any cycles.
        
        def dfs(course):
            # checking for cycles
            if course in visited:
                return False
            
            # checking if course has 0 pre reqs
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visited.remove(course)
            preMap[course] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
        
        