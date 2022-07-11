class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_arr = []
        count = 0
        new_arr = sorted(heights)
        
        for i in range(len(new_arr)):
            if new_arr[i] != heights[i]:
                count += 1
        return count  