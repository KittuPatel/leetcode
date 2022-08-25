class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_sum = float("inf")
        
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                sum_val = nums[i] + nums[l] + nums[r]
                
                if abs(target - sum_val) < abs(target-best_sum):
                    best_sum = sum_val
                
                if sum_val == target:
                    return target
                elif sum_val < target:
                    l += 1
                else:
                    r -= 1
                    
        return best_sum
                
                
                