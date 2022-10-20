class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        results = []
        
        def dfs(n, subset, start, result):

            while start * start <= n:
                if n % start == 0:
                    result.append(subset + [start, n//start])
                    dfs(n//start, subset + [start], start, result)

                start += 1

            return result
        
        dfs(n, [], 2, results)
        return results