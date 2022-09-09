# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                start = mid + 1
                
            else:   
                end = mid - 1
        return start
    
#     r = n-1
#     l = 0
#     while(l<=r):
#         mid = l + (r-l)/2
#         if isBadVersion(mid)==False:
#             l = mid+1
#         else:
#             r = mid-1
#     return l