class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hashmap = {}
        for i, word in enumerate(wordsDict):
            if word not in self.hashmap:
                self.hashmap[word] = [i]
            else:
                self.hashmap[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float("inf")
        for word1idx in self.hashmap[word1]:
            for word2idx in self.hashmap[word2]:
                res = min(res, abs(word1idx - word2idx))
                
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)