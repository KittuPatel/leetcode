class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        se = sorted(list(set(nums)))
        n = len(se)

        if n < 3:
            return max(nums)
        return se[n-3]

            