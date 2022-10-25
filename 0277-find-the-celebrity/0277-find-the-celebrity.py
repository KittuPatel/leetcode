# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# from functools import cache

class Solution:
    
    # @cache
    # def cached_knows(self, a, b) -> bool:
    #     return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:        
        # logic:
        #   - if i knows celeb, celeb remains
        #   - if celeb knows i, celeb invalidated and i is new candidate celeb
        #       - in this case:
        #           - i is only person up to this point that may NOT know anyone else
        #   - last pass checks "surviving" candidate
        # 
        # could use a cached version `self.cached_knows` to reduce "API" calls 
        celeb = 0
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i

        for i in range(n):
            if i != celeb:
                if not knows(i, celeb) or knows(celeb, i):
                    return -1
        
        return celeb