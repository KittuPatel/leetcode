class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findMinimumElementIndex(self, nums):
            start = 0
            end = len(nums) - 1
            n = len(nums)
            while start <= end:
                mid = start + ((end - start) // 2)
                
                prev = (mid - 1 + n) % n
                next = (mid + 1) % n
                
                if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
                    return mid
                elif nums[mid] <= nums[end]:
                    end = mid - 1
                elif nums[mid] >= nums[start]:
                    start = mid + 1
    
        
        minIndex = findMinimumElementIndex(self, nums)
        
        def binary_search(self, nums, start, end):
            while start <= end:
                mid = start + ((end - start) // 2)
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        start = 0
        end = len(nums) - 1
        
        l = binary_search(self, nums, start, minIndex - 1)
        r = binary_search(self, nums, minIndex, end)
        return max(l,r)
            