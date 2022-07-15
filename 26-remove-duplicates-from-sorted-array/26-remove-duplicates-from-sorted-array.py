class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        r = 1
        for i in range(1, len(nums)):
            if (nums[r] != nums[r-1]):
                nums[l] = nums[r]
                l += 1
            r += 1
                
            
        return l
                