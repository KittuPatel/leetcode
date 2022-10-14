class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
#         Bruteforce
#         minDistance = len(wordsDict)
        
#         for i in range(len(wordsDict)):
#             if wordsDict[i] == word1:
#                 for j in range(len(wordsDict)):
#                     if wordsDict[j] == word2:
#                         minDistance = min(minDistance, abs(i-j))
                        
#         return minDistance


        i1, i2 = -1, -1
        minDistance = len(wordsDict)
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                minDistance = min(minDistance, abs(i1-i2))
                
        return minDistance