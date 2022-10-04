from functools import cache
class Solution:
    def numTrees(self, n: int) -> int:
        return self._helper(n)
    
    @cache
    def _helper(self, n: int) -> int:
        if n == 0:
            return 1

        if n == 1:
            return 1
 
        result = 0
        for i in range(n):
            left = self._helper(i)
            right = self._helper(n - i - 1)
            result += left * right

        return result


# class Solution:
#     def numTrees(self, n: int) -> int:
            
#         numTree = [1] * (n+1)
        
#         # we already have it for nodes 1 and 2
#         for nodes in range(2, n+1):
#             total = 0
#             for root in range(1, nodes +1):
#                 left = root - 1
#                 right = nodes - root
                
#                 total += (numTree[left] * numTree[right])
                
#             numTree[nodes] = total
            
#         return numTree[n]