class Solution:
    def climbStairs(self, n: int) -> int:
#         one, two = 1, 1
        
#         for i in range(n-1):
#             temp = one
#             one = one + two
#             two = temp
        
        
#         return one

        # def climb(n):  # inner func to make life easier
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = climb(n-1) + climb(n-2)
        #         return memo[n]
        # memo = {1: 1, 2: 2}  # base cases
        # return climb(n)
        
        if n == 1 or n == 2:
            return n
        
        dp = [0] * n
        
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]
 
     
    
        