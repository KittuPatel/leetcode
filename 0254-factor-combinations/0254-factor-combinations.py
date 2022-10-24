class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        res = []              # final result
        factors = []          # one possible combination of factors
        
        def dfs(start, x):
            if factors:       # ensure x != n
                res.append(factors + [x])
            for factor in range(start, int(sqrt(x))+1):  # set upbound to sqrt(x) to ensure x/factor >= factor
                if x%factor == 0:
                    factors.append(factor)
                    dfs(factor, x/factor)
                    factors.pop()
        dfs(2, n)
        return res