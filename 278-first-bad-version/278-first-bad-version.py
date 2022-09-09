# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        res = end
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid - 1
                res = mid
            else:               
                start = mid + 1
        return res
