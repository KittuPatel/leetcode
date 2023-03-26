class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = {}
        
        for n in nums:
            
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        for key, value in hashmap.items():
            # print(key, value)
            if value > len(nums) // 2:
                return key