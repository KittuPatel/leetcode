class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # scan front pre fix
        
        # scan from back - post fix
        res = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre = pre * nums[i]
        
        post = 1
        for i in reversed(range(len(nums))):
            res[i] *= post
            post = post * nums[i]
        
        return res