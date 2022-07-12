class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #    O(nlogn) solution
#         res = [0] * len(nums)
#         for i in range(len(nums)):
#             res[i] = nums[i] * nums[i]
                
#         res.sort()  
#         return res
        
        # O(n) solution
        res = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                res.append(nums[i] * nums[i])
                i += 1
            else:
                res.append(nums[j] * nums[j])
                j -= 1  

        return res[::-1]