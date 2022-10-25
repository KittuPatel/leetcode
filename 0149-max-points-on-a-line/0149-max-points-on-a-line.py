class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # calculate slope
        hashmap = {}
        max_points = 0
        
        for i in range(len(points)):
            i_max = 0
            for j in range(i+1, len(points)):
                # slope = (y2 - y1)/(x2-x1)
                # to avoid zero division error: denominator 
                if (points[j][0] - points[i][0]) == 0:
                    slope = float("inf")
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                
                if slope in hashmap:
                    hashmap[slope] += 1
                else:
                    hashmap[slope] = 1
                    
                i_max = max(i_max, hashmap[slope])
            hashmap.clear() 
            max_points = max(max_points, i_max)
                    
        return max_points+1