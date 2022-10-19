class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        res = []
        
        for idx, num in enumerate(nums):
            nums[idx] = (a*num*num) + (b*num) + c
            
        i, j = 0, len(nums)-1
        # three cases 
        if a > 0:
            while i <= j:
                if nums[i] > nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j -= 1
        
        elif a < 0:
            while i <= j:
                if nums[i] < nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j -= 1
        
        # if a == 0
        else:
            if b > 0:
                return nums
            else:
                return nums[::-1]
            
        
        return res if a < 0 else res[::-1]
                
            