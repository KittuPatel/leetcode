class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1: return True
        
        def custom_sqrt(num):
            
            lo, hi = 0, num
            
            while lo <= hi:
                mid = (lo+hi) // 2
                
                if mid*mid > num:
                    hi = mid-1
                elif mid*mid < num:
                    lo = mid+1
                else:
                    return mid
                
        return True if isinstance(custom_sqrt(num), int) else False