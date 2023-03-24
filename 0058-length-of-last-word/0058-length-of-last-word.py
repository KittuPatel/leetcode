class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # arr = s.split()
        # return len(arr[-1])
        
        
        length = 0
        i = len(s) - 1
        
        for j in range(len(s) -1, -1, -1):
            if s[j] == " ":
                i -= 1
            else:
                break
        
        
        while i >= 0:
            if s[i] != " ":
                length += 1
            else:
                return length
            i -= 1
                
        return length