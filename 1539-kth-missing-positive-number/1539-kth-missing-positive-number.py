class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # binary search
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low+high)//2
            
            missingTillMid = arr[mid] - (mid + 1)
            if missingTillMid < k:
                low = mid+1
            else:
                high = mid - 1
            
        return low +k
        
        
        # brute force
#         res = []
        
#         for i in range(1, max(arr)):
#             if i not in arr:
#                 res.append(i)
#         print(res)
        
#         if len(res) < k:
#             return arr[-1] - len(res) + k
#         else:
#             return res[k-1]