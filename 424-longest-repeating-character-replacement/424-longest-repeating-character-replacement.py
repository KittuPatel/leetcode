class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        scount = {}
        start = 0
        res = 0
        
        for end in range(len(s)):
            scount[s[end]] = 1 + scount.get(s[end], 0)
            # window size - max of count values gives us letter count that can be replaced
#             if number of replacements is greater than the number of replacements allowed then execute below code. shift left pointer
            while (end - start + 1) - max(scount.values()) > k:
                scount[s[start]] -= 1
                start += 1
            
            res = max(res, end - start + 1)
            
        return res
                
            