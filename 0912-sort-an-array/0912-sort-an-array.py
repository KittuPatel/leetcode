class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, left, right):
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                
                k += 1
                
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                
            return arr
        
        def divide(arr):
            
            if len(arr) == 1:
                return arr
            
            # find midpoint
            m = len(arr) // 2
            left = arr[:m]
            right = arr[m:]
            divide(left)
            divide(right)
            
            return merge(arr, left, right)  
                
        
        return divide(nums)
                
                
                
                