class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        output = []
        
        preMap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visited, cycle = set(), set()
        
        # 3 possible states
        # visited, visiting, unvisited
        
        
        
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True
            
            cycle.add(crs)
            
            for pre in preMap[crs]:
                if dfs(pre) == False: 
                    return False
                
            cycle.remove(crs)
            visited.add(crs)
            
            output.append(crs)
                
        for crs in range(numCourses):
            if dfs(crs) == False: 
                return []
        
        return output
            