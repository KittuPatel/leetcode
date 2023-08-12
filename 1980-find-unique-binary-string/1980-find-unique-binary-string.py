class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        s = "01"
        res = []
        
        def dfs(i, curStr):
            
            if len(curStr) == n:
                if curStr not in nums:
                    res.append(curStr)
                return
                    
            for i in range(2):
                curStr = curStr+s[i]
                dfs(i+1, curStr)
                curStr = curStr[:-1]
            
        dfs(0, "")
        return res[0]