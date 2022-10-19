class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        result = []
        heapq.heapify(result)
        
        for x in nums:
            ans = (a*x*x) + (b*x) + c
            heapq.heappush(result, ans)
            
        return list(heapq.nsmallest(len(nums), result))