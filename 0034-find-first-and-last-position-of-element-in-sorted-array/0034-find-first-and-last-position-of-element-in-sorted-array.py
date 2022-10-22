class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        def binary_search(leftBias):
            l = 0
            r = len(nums)-1
            i = -1
            while l<= r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            return i
                     
            
        left = binary_search(True)
        right = binary_search(False)
        
        return [left, right]
        
        