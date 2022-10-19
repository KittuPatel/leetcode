class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def recur(n):
            if n in memo: return memo[n]
            ans = set()
            for i in range(2, int(sqrt(n))+1):
                if n%i == 0:
                    ans.add((i, n//i))
                    for j in recur(n//i):
                        ans.add(tuple(sorted([i, *j])))
            memo[n] = ans
            return ans
        memo = defaultdict(set)
        return recur(n)