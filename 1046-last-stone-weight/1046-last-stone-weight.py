class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) >= 1:
            if len(stones) == 1:
                return stones[0]
            
            max1 = max(stones)
            max1idx = stones.index(max1)
            stones.pop(max1idx)
            
            max2 = max(stones)
            max2idx = stones.index(max2)
            stones.pop(max2idx)
            
            diff = abs(max1-max2)
            if diff > 0: 
                stones.append(diff)
            
        return 0