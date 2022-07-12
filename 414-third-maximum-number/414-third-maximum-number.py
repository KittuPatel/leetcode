class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        se = sorted(list(set(nums)))
        n = len(se)

        if n < 3:
            return max(nums)
        return se[n-3]
    
    
#         MAX1, MAX2, MAX3 = float('-inf'),float('-inf'),float('-inf')        
#             for j in range(len(arr)):
#                if arr[j] > MAX1:
#                 MAX3 = MAX2
#                 MAX2 = MAX1
#                 MAX1 = arr[j]            
#                elif arr[j] > MAX2 and arr[j] < MAX1:
#                 MAX3 = MAX2
#                 MAX2 = arr[j]
#                elif arr[j] > MAX3 and arr[j] < MAX2:
#                 MAX3 = arr[j]  

#             if MAX3 == float('-inf'):
#                return max(MAX2, MAX1)
#             else:
#                return MAX3

            