class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # o(m.n) solution
#         ans = [-1] * len(nums1)
#         nums1IdxMap = {n:i for i, n in enumerate(nums1)}
        
#         for i in range(len(nums2)):
#             if nums2[i] not in nums1IdxMap:
#                 continue
                
#             for j in range(i+1, len(nums2)):
#                 if nums2[j] > nums2[i]:
#                     idx = nums1IdxMap[nums2[i]]  
#                     ans[idx] = nums2[j]
#                     break
                    
#         return ans


        # o(m+n) solution
        
        ans = [-1] * len(nums1)
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        
        # stack
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                ans[idx] = cur
            
            if cur in nums1Idx:
                stack.append(cur)
            
        return ans
            
            
            
        
        
        
        
        
        
        
        
            
                
                
                