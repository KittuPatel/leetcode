class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # start, end = 0, len(letters) - 1
        
        for i in letters:
            if i > target:
                return i
        return letters[0]
                