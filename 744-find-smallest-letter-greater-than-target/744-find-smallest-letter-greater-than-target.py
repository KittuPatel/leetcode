class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # O(n) solution
        # for i in letters:
        #     if i > target:
        #         return i
        # return letters[0]
    
        # O(logn) solution
        start, end = 0, len(letters) - 1
        charRes = letters[0]
        
        while start <= end:
            mid = (start + end) // 2 
            
            if target < letters[mid]:
                charRes = letters[mid]
                end = mid - 1
            else:
                start = mid + 1
                
        return charRes
                 