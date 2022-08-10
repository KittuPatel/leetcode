class Solution:
    
    def findPivot(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid
            elif mid > start and nums[mid] < nums[mid - 1]:
                return mid - 1
            elif nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return start
        
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
    
        
    def binarySearch(self, nums, start, end, target):
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        pivotIndex = self.findMinimumElementIndex(nums)
        print(pivotIndex)
        targetIndex = self.binarySearch(nums, 0, pivotIndex - 1, target)
        return targetIndex if targetIndex != -1 else self.binarySearch(nums, pivotIndex, len(nums)-1, target)
        
        # l = binary_search(self, nums, start, minIndex - 1, target)
        # r = binary_search(self, nums, minIndex + 1, end, target)

            