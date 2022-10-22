class Solution:

    def __init__(self, w: List[int]):
        #prefix_sums
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
            

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        
        l, h = 0, len(self.prefix_sums)
        while l<h:
            mid = (l+h)//2
            if target > self.prefix_sums[mid]:
                l = mid + 1
            else:
                h = mid
        
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()