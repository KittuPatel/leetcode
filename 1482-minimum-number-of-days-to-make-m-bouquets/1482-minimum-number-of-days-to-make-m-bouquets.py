class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m*k : return -1
        
        def isPossible(numOfDays):
            cnt = 0
            numOfB = 0
            for day in bloomDay:
                if day <= numOfDays:
                    cnt +=1
                else:
                    numOfB += (cnt//k)
                    cnt = 0
            numOfB += (cnt//k)
            return numOfB >= m
        
        low, high = min(bloomDay), max(bloomDay)
        ans = 0
        
        while low <= high:
            mid = (low + high)//2
            
            if isPossible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans