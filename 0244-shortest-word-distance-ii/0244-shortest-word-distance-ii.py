from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hashmap = defaultdict(list)
        
        for idx, word in enumerate(wordsDict):
            self.hashmap[word].append(idx)
        
        print(self.hashmap)

    def shortest(self, word1: str, word2: str) -> int:
        res = float("inf")
        for w1i in self.hashmap[word1]:
            for w2i in self.hashmap[word2]:
                res = min(res, abs(w1i-w2i))  
        
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)