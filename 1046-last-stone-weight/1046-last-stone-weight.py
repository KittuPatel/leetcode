import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        
        heapq.heapify(stones)
        
        # atleast 2 are there
        while len(stones) > 1:
            
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            first = abs(first)
            second = abs(second)
            
            diff = first - second
            
            if first > second:
                heapq.heappush(stones, diff*-1)
            
        stones.append(0)
        return abs(stones[0])
            
            
        
#         while len(stones) >= 1:
#             if len(stones) == 1:
#                 return stones[0]
            
#             max1 = max(stones)
#             max1idx = stones.index(max1)
#             stones.pop(max1idx)
            
#             max2 = max(stones)
#             max2idx = stones.index(max2)
#             stones.pop(max2idx)
            
#             diff = abs(max1-max2)
#             if diff > 0: 
#                 stones.append(diff)
            
#         return 0

