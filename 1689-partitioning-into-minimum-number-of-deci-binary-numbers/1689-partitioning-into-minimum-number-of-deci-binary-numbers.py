class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        
        for c in n:
            if int(c) > res:
                res = int(c)
                
        return res