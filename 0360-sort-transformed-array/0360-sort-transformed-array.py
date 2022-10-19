from sortedcontainers import SortedList

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        # nums = SortedList(nums)
        
        for i in range(len(nums)):
            nums[i] = (a* pow(nums[i], 2)) + (b*nums[i]) + c
        
        nums.sort()
        
        return nums