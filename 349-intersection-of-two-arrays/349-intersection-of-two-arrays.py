class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = set(nums1)
        l2 = set(nums2)
        res = []
        for num in l1:
            if num in l2:
                res.append(num)
                
        return res