class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
            
        nums.sort()
        res = []
        for num in nums:
            res.append(num*num)
        return res