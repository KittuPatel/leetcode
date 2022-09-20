class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
    # multiply from both front and back
        A = nums
        B = nums[::-1]
        
        for i in range(1, len(A)):
            if A[i-1] != 0:
                A[i] *= A[i-1]
            
            if B[i-1] != 0:
                B[i] *= B[i-1]
        
        maxA = max(A)
        maxB = max(B)
        
        return max(maxA, maxB)
         