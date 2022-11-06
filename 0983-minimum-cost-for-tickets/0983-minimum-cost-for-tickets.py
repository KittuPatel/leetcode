class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        N = len(days)
        def dfs(i):
            if i == len(days):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = float("inf")
            j = i
            # d = number of days we are gonna travel
            # c = cost for travelling that many number of days
            # O(38.n)
            for d, c in zip([1,7,30], costs):
                while j < N and days[j] < days[i] + d:
                    j += 1
                cache[i] = min(cache[i], c + dfs(j))
                
            return cache[i]
        
        return dfs(0)
        