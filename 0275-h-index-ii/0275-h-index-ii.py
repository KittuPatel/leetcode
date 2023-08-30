class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left = 0
        right = len(citations) - 1
        h_index = 0
        
        # Binary search
        while left <= right:
            mid = (left + right) // 2
            better_papers = len(citations) - mid
            
            if citations[mid] <= better_papers:  # This means the citation value can be used a h_index
                h_index = max(h_index, citations[mid])
                left = mid + 1

            else: 
                h_index = max(h_index, better_papers)
                right = mid - 1
        
        return h_index