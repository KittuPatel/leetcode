class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        left, right = 0, 0
        count = 0
        product = 1
        
        if k <= 1:
            return 0
        
        while right < len(nums):
            
            product *= nums[right]
            
            while product >= k:
                product = product // nums[left]
                left += 1
            
            count += (right - left + 1)
            right += 1
        
        return count
        
                
                    