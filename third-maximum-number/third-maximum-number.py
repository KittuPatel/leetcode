from heapq import *
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
#         se = sorted(list(set(nums)))
#         n = len(se)

        # if len(nums) < 3:
        #     return max(nums)
    
    
#         O(n) solution
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


#           O(n) Solution

        S = []
        
        for x in set(nums):
            if len(S) < 3:
                heapq.heappush(S, x)
            else:
                heapq.heappushpop(S, x)
                
        return S[0] if len(S) == 3 else max(S)



            