class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        adjMap = collections.defaultdict(list)
        
        for i in range(n):
            adjMap[manager[i]].append(i)
        
        q = collections.deque([(headID, 0)])
        res = 0
        
        while q:
            mgr, time = q.popleft()
            
            for emp in adjMap[mgr]:
                q.append((emp, time+informTime[mgr]))
            res = max(res, time)
        return res
        
        