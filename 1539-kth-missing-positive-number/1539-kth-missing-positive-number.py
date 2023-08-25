class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        res = []
        
        for i in range(1, max(arr)):
            if i not in arr:
                res.append(i)
        print(res)
        
        if len(res) < k:
            return arr[-1] - len(res) + k
        else:
            return res[k-1]