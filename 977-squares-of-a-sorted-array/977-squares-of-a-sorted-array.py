class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
#         O(nlogn) solution
#         for i in range(len(nums)):
#             nums[i] = abs(nums[i])
            
#         nums.sort()
#         res = []
#         for num in nums:
#             res.append(num*num)
#         return res


#    O(n) solution
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
    
        minVal = nums.index(min(nums))
        res = []
        left, right = minVal - 1, minVal + 1
        
        res.append(nums[minVal] * nums[minVal])
        
        while left >= 0 and right < len(nums):
            if nums[left] < nums[right]:
                res.append(nums[left] * nums[left])
                left -= 1
            else:
                res.append(nums[right] * nums[right])
                right += 1
        
        while left >= 0:
            res.append(nums[left] * nums[left])
            left -= 1
        
        while right < len(nums):
            res.append(nums[right] * nums[right])
            right += 1

        return res
        
        