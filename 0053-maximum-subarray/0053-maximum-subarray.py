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