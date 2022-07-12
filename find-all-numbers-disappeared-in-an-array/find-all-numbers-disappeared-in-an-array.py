class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            
        print(nums)
        
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res