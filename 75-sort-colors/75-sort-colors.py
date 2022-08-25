class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high = 0, len(nums) - 1
        i = 0 # moving pointer
        
        while i <= high:
            if nums[i] == 0: # if number is 0
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                i += 1
            elif nums[i] == 1: # if number is 1
                i += 1
            else: # if number is 2
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
        
        
                 