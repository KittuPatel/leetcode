class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        smapt, tmaps = {}, {}
        
        for c1, c2 in zip(s, t):
            
            if ((c1 in smapt and smapt[c1] != c2) or 
                (c2 in tmaps and tmaps[c2] != c1)):
                return False
            
            smapt[c1] = c2
            tmaps[c2] = c1
            
        return True