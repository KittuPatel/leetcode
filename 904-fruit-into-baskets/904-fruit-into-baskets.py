class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        maxLen = 0
        dict = {}
        
        for end in range(len(fruits)):
            if fruits[end] not in dict:
                dict[fruits[end]] = 0
            dict[fruits[end]] += 1
            
            while len(dict) > 2:
                dict[fruits[start]] -= 1
                if dict[fruits[start]] == 0:
                    del dict[fruits[start]]
                start += 1
                
            maxLen = max(maxLen, end - start + 1)
        
        return maxLen