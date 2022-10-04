class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # reference = leetcode video
        dp = [0] * (len(triangle) + 1)
        res = 0
        # dp = 0 0 0 0 0
        for row in triangle[::-1]:
            for i, num in enumerate(row):
                dp[i] = num + min(dp[i], dp[i+1])
        return dp[0]
    