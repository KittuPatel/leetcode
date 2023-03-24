class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)    

        # for char in s:
        #     i = t.find(char)
        #     if i == -1: 
        #         return False
        #     else:
        #         t = t[i+1:]
        # return True
                
        