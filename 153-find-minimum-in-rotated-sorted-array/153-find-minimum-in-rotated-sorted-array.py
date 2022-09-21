class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n-1
        
        while start <= end:
            mid = (start + end) // 2
            prev = (mid - 1 + n) % n
            nex = (mid + 1) % n
            
            if nums[mid] < nums[prev] and nums[mid] < nums[nex]:
                return nums[mid]
            elif nums[mid] < nums[start]: 
#                 right array is sorted so go left
                end = mid-1
            elif nums[mid] > nums[end]: 
                start = mid+1
            else:
                return nums[start]
        
 

       
#         # if not selecting the unsorted part of array
#         elif arr[mid]<arr[start]: end = mid-1
#         elif arr[mid]>arr[end]: start = mid+1
#         else: return 0
        