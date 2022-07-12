class Solution:
    def thirdMax(self, nums: List[int]) -> int:
#         convert to set and then list
        se = sorted(list(set(nums)))
        n = len(se)
        print(se)
        if n < 3:
            return max(nums)
        return se[n-3]
#         for i in nums(n-1, -1, n-4):
#             num = nums[n-4]
        
#         return num
            
# sorted
# for loop back

            