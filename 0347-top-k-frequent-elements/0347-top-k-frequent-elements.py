import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        
        for n in nums:
            d[n] = 1 + d.get(n, 0)
            
        heap = [(val, key) for key, val in d.items()]
        
        most_frequent = heapq.nlargest(k, heap)
        
        res = []
        
        for i in range(k):
            res.append(most_frequent[i][1])
            
        return res