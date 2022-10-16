class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        res = 0
        for box in boxTypes:
            
            if box[0] < truckSize:
                res += box[0] * box[1]
                truckSize -= box[0]
            
            elif box[0] >= truckSize:
                res += truckSize * box[1]
                break
        
        return res
            
            
            