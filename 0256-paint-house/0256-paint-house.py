class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prevHouse = [0, 0, 0]
        
        for i in range(len(costs)):
            dp0 = costs[i][0] + min(prevHouse[1], prevHouse[2])
            dp1 = costs[i][1] + min(prevHouse[0], prevHouse[2])
            dp2 = costs[i][2] + min(prevHouse[0], prevHouse[1])
            
            prevHouse = [dp0, dp1, dp2]
        
        return min(prevHouse)