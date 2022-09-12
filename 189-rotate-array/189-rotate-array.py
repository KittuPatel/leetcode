class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #         Bad solution
        #         for i in range(k):
        #             last = nums[len(nums) - 1]
        #             nums.pop()
        #             nums.insert(0, last)

        #         return nums

        # O(n) space and time
        #  put every element in i + k index
        #         res = [0] * len(nums)
        #         for idx, num in enumerate(nums):
        #             pos = (idx + k) % len(nums)
        #             print(pos)
        #             res[pos] = num
        #             print(num)

        #         for i in range(len(nums)):
        #             nums[i] = res[i]
    
        # O(n) Time | O(1) space solution   
        # reverse nums, then again reverse first k elements and then reverse other              half
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        
        
        

        