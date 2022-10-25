class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        res = []              # final result
        factors = []          # one possible combination of factors
        
        def dfs(start, num):
            if factors:       # ensure num != n
                res.append(factors + [num])
            for factor in range(start, int(sqrt(num))+1):  
                # set upbound to sqrt(num) to ensure num/factor >= factor
                if num%factor == 0:
                    factors.append(factor)
                    dfs(factor, num/factor)
                    factors.pop()
        dfs(2, n)
        return res