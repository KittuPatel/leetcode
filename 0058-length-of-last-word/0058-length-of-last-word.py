class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # arr = s.split()
        # return len(arr[-1])
        
        
        length = 0
        i = len(s) - 1
        
        while s[i] == " ":
            i -= 1
        
        while i >= 0:
            if s[i] != " ":
                length += 1
            else:
                return length
            i -= 1
                
        return length