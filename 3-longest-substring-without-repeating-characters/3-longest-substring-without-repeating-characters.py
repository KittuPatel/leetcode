class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        maxLen = 0
        start = 0
        
        for end in range(len(s)):
            right = s[end]
            
            if right in dict:
                start = max(start, dict[right] + 1)
            dict[right] = end
            
            maxLen = max(maxLen, end - start + 1)
        
        return maxLen