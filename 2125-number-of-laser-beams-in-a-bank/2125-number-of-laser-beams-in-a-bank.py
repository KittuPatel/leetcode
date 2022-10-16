class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prevCount = 0
        
        for s in bank:
            count = s.count('1')
            
            if count == 0:
                continue
                
            res += prevCount * count
            prevCount = count
        
        return res