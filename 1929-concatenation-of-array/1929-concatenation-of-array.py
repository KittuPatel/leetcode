class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = nums.copy()
        
        for n in nums:
            ans.append(n)
            
        return ans
        
        
        