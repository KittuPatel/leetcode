class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        s = "01"

        def dfs(i, curStr):
            
            if len(curStr) == n:
                if curStr not in nums:
                    return curStr
                return None
                    
            for i in range(2):
                curStr = curStr+s[i]
                res = dfs(i+1, curStr)
                if res is not None:
                    return res
                curStr = curStr[:-1] 
            
        return dfs(0, "")