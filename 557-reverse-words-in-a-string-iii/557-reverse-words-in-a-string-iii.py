class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = s.split(" ")
        arr = [word[::-1] for word in arr]            
        return " ".join(arr)
