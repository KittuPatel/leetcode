class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = len(wordsDict)
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                for j in range(len(wordsDict)):
                    if wordsDict[j] == word2:
                        minDistance = min(minDistance, abs(i-j))
                        
        return minDistance