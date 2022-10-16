class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        
        for i in range(len(boxes)):
            k = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    k += abs(i-j)
            res.append(k)
            
        return res