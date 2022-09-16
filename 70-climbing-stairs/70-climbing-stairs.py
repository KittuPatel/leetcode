class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         one, two = 1, 1
        
#         for i in range(n-1):
#             temp = one
#             one = one + two
#             two = temp
        
#         return one
    
    # Bottom up, O(n) space
    def climbStairs(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
            
        