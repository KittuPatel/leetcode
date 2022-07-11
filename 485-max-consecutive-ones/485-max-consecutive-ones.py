class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = temp = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:
                if temp < count:
                    temp = count
                count = 0
        return max(count, temp)
        