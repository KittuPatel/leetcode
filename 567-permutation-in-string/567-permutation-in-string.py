class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        s1count = {}
        s2count = {}
        
        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
        
        start = 0
        k = len(s1)

        for end in range(len(s2)):
            rightChar = s2[end]
            if end - start + 1 <= k:
                s2count[rightChar] = 1 + s2count.get(rightChar, 0)
            else:
                s2count[s2[start]] -= 1
                if s2count[s2[start]] == 0:
                    del s2count[s2[start]]
                start += 1
                s2count[s2[end]] = 1 + s2count.get(s2[end], 0)
            
            if s1count == s2count:
                return True
        
        return False
    
    
#     s1_count = Counter(s1)
#         s2_count = Counter()
#         start = 0
#         window = len(s1)
        
#         for end, c in enumerate(s2):
#             if end - start + 1 <= window:
#                 s2_count[c] += 1
#             else:
#                 s2_count[s2[start]] -= 1
#                 start += 1
#                 s2_count[c] += 1
#             if s1_count == s2_count:
#                 return True
        
#         return False
                
                
                
            
            
        