import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def isPossible(possibleNum):
            totalSum = 0
            for n in nums:
                totalSum += math.ceil(n/possibleNum)
            if totalSum <= threshold: return True
            return False
        
        low, high = 1, max(nums)
        ans = float("inf")
        while low <= high:
            mid = (low+high)//2
            
            if isPossible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
                
        return ans
            