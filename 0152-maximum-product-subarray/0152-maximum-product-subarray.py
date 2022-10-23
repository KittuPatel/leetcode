class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # maintain curMin and curMax
        res = max(nums)
        
        curMin, curMax = 1, 1
        
        for num in nums:
            
            if num == 0:
                curMin, curMax = 1, 1
            
            tmp = num*curMax
            curMax = max(num*curMax, num*curMin, num)
            curMin = min(tmp, num*curMin, num)
            res = max(res, curMax, curMin)
            
        return res
        
            