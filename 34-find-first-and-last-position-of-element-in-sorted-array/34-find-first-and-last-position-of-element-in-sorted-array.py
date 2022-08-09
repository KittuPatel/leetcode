class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        res = [-1, -1]
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                res[0] = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        start = 0
        end = len(nums) - 1
            
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                res[1] = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return res