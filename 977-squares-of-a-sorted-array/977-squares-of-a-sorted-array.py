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


#    O(n) solution but little but annoying
        
        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i])
    
        minVal = nums.index(min(nums, key = abs))
        res = []
        left, right = minVal - 1, minVal + 1
        
        res.append(nums[minVal] * nums[minVal])
        
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
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

# O(n) using left and right pointers and finding max value and returning reverse

#         res = []
#         left, right = 0, len(nums) - 1
        
#         while left <= right:
#             if nums[left] * nums[left] > nums[right] * nums[right]:
#                 res.append(pow(nums[left], 2))
#                 left += 1
#             else:  
#                 res.append(pow(nums[right], 2))
#                 right -= 1
        
#         return res[::-1]
        
        
        