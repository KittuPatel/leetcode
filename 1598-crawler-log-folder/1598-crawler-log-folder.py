class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        
        for s in logs:
            if s == "./":
                continue
            elif s == "../":
                res -= 1
                if res < 0: res = 0
            else:
                res += 1
        
        return res
        
        