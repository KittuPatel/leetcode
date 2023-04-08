import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        
        # index is count, val is num
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
            
        for num, count in hashmap.items():
            freq[count].append(num)
        
        res = []
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
        
        return res
        
        
#         d = {}
        
#         for n in nums:
#             d[n] = 1 + d.get(n, 0)
            
#         heap = [(val, key) for key, val in d.items()]
        
#         most_frequent = heapq.nlargest(k, heap)
        
#         res = []
        
#         for i in range(k):
#             res.append(most_frequent[i][1])
            
#         return res