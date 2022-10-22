class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        data = []
        
        for s, e in intervals:
            data.append((s, 1))
            data.append((e, -1))
        
        data.sort()
        
        cur, res = 0, 0
        
        for _, val in data:
            cur += val
            res = max(res, cur)
            
        return False if res > 1 else True