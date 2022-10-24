class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsMap = collections.defaultdict(list)
        
        for idx, word in enumerate(wordsDict):
            self.wordsMap[word].append(idx)        

    def shortest(self, word1: str, word2: str) -> int:
        res = float("inf")
        
        for idx1 in self.wordsMap[word1]:
            for idx2 in self.wordsMap[word2]:
                res = min(res, abs(idx1-idx2))
                
        
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)