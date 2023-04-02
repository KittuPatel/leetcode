class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         hashset = set()
        
#         for n in nums:
#             hashset.add(n)
            
            
#         result = []
        
#         for i, n in enumerate(nums):
#             if (i + 1) not in hashset:
#                 result.append(i+1)
                
#         return result

        
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -1 * abs(nums[idx])
            
        res = []
        
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
            
        return res
            


