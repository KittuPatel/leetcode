class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        d = {}
        
        for char in text:
            
            d[char] = 1 + d.get(char, 0)
            
        print(d)
        output = 0
        
        while True:
            for char in "balloon":   
                if char in d:
                    d[char] -= 1
                    if d[char] == 0:
                        d.pop(char)
                else:
                    return output

            output += 1
                
        
        return output
            
            
            
            