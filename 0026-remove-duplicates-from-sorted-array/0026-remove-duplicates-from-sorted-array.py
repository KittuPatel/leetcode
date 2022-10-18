class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # if len(nums) == 1: return 1
        # i = 0
        # while i < len(nums)-1:
        #     if nums[i] == nums[i+1]:                
        #         nums.pop(i+1)  
        #     else:    
        #         i += 1
        # return i + 1
            
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        return l
                    
        