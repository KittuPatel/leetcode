class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = []
        
        prev = 0
        for n in nums:
            prev += n
            
            leftSum.append(prev)
            
        print(leftSum)
        
        rightSum = []
        
        prev = 0
        for n in reversed(nums):
            prev += n
            
            rightSum.append(prev)
            
        rightSum = rightSum[::-1]
        
        for i, (n1, n2) in enumerate(zip(leftSum, rightSum)):
            if n1 == n2:
                return i
        
        return -1
        
        # l = 2, 3, 2
        # r = 2 ,0 ,-1