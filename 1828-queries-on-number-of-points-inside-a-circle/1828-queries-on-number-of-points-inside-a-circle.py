class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        for query in queries:
            x_coord, y_coord, radius = query
            temp = 0
            for point in points:
                point_x, point_y = point
                
                e_distance = pow(point_x - x_coord, 2) + pow(point_y - y_coord, 2)
                
                if e_distance <= pow(radius, 2):
                    temp += 1
            
            res.append(temp)
            
        return res
                