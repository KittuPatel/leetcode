class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        
        while l < len(prices) and r < len(prices):
            if prices[r] < prices[l]:
                l = r

            else:
                temp = prices[r] - prices[l]
                profit = max(profit, temp)
            r += 1
        
        return profit
            
        