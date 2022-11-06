class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # build expressions
        # only '+' and '-' , so 2^n choices
        # return the num of expressions
        
        dp = {} # (index, sum) -> # of ways

        def backtrack(index, total):
            if index == len(nums):
                return 1 if target == total else 0
            
            if (index, total) in dp:
                return dp[(index, total)]
            
            dp[(index, total)] = (backtrack(index+1, total+nums[index]) + backtrack(index+1, total-nums[index]))

            return dp[(index, total)]
        

        return backtrack(0, 0)


