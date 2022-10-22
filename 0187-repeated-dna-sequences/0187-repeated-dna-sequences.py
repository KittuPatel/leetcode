class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dict = {}
        
        res = []
        
        for x in range(len(s)-9):
            if s[x:x+10] not in dict:
                dict[s[x:x+10]] = 0
            dict[s[x:x+10]] += 1
        
        
        for key, val in dict.items():
            if val > 1:
                res.append(key)
        
        return res
            