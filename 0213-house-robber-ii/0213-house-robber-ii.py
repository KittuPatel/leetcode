class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            rob1, rob2 = 0, 0

            for num in nums:
                newRob = max(num+rob1, rob2)
                rob1 = rob2
                rob2 = newRob
                
            return rob2
        
        
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))