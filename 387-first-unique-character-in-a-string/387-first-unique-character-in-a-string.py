class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for c in s:
            dict[c] = 1 + dict.get(c, 0)
        
        for idx, c in enumerate(s):
            if dict[c] == 1:
                return idx
        return -1
        