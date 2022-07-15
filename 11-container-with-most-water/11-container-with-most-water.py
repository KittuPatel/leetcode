class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        
        while (i <= j):
            min_ele = min(height[i], height[j])
            area = min_ele * (j-i)
            max_area = max(max_area, area)
            
            if (min_ele == height[i]):
                i += 1
            else:
                j -= 1
        return max_area