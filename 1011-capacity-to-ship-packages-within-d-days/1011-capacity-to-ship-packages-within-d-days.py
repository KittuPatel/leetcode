class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isPossible(capacity):
            daysCount = 1
            load = 0
            for weight in weights:
                if weight + load > capacity:
                    daysCount += 1
                    load = weight
                else:
                    load += weight
            
            if daysCount <= days:
                return True
            else:
                return False
                
        
        low, high = max(weights), sum(weights)
        ans = float("inf")
        
        while low <= high:
            mid = (low+high)//2
            
            if isPossible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans