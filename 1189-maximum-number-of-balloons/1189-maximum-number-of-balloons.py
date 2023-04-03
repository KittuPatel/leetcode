class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        countText = {}
        for char in text:
            countText[char] = 1 + countText.get(char, 0)
                
        balloon = {}
        for char in "balloon":
            balloon[char] = 1 + balloon.get(char, 0)
        
        
        res = float("inf")
        
        for char in balloon:
            if char in countText:
                res = min(res, countText[char] // balloon[char])
            else:
                res = 0
        
        return res
            
            
            
            
            
#         print(d)
#         output = 0
        
#         while True:
#             for char in "balloon":   
#                 if char in d:
#                     d[char] -= 1
#                     if d[char] == 0:
#                         d.pop(char)
#                 else:
#                     return output

#             output += 1
                
        
#         return output
            
            
            
            