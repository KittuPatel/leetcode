class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not len(strs):
#             return ''
        
#         i = 0
#         for i, chars in enumerate(zip(*strs), 1):
#             if len(set(chars)) != 1:
#                 i -= 1
#                 break
        
#         return strs[0][:i]
    
        res=''
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res  