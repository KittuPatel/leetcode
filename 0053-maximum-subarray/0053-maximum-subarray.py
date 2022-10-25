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

# divide and conquer
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         def findBestSubarray(nums, left, right):
#             # Base case - empty array.
#             if left > right:
#                 return -math.inf

#             mid = (left + right) // 2
#             curr = best_left_sum = best_right_sum = 0

#             # Iterate from the middle to the beginning.
#             for i in range(mid - 1, left - 1, -1):
#                 curr += nums[i]
#                 best_left_sum = max(best_left_sum, curr)

#             # Reset curr and iterate from the middle to the end.
#             curr = 0
#             for i in range(mid + 1, right + 1):
#                 curr += nums[i]
#                 best_right_sum = max(best_right_sum, curr)

#             # The best_combined_sum uses the middle element and
#             # the best possible sum from each half.
#             best_combined_sum = nums[mid] + best_left_sum + best_right_sum

#             # Find the best subarray possible from both halves.
#             left_half = findBestSubarray(nums, left, mid - 1)
#             right_half = findBestSubarray(nums, mid + 1, right)

#             # The largest of the 3 is the answer for any given input array.
#             return max(best_combined_sum, left_half, right_half)
        
#         # Our helper function is designed to solve this problem for
#         # any array - so just call it using the entire input!
#         return findBestSubarray(nums, 0, len(nums) - 1)
