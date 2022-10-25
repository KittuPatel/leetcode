# bruteforce
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_subarray = -math.inf
#         for i in range(len(nums)):
#             current_subarray = 0
#             for j in range(i, len(nums)):
#                 current_subarray += nums[j]
#                 max_subarray = max(max_subarray, current_subarray)
        
#         return max_subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        # Dynamic Programming, Kadane's Algorithm
        for end in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[end]
            maxSub = max(maxSub, curSum)
        return maxSub