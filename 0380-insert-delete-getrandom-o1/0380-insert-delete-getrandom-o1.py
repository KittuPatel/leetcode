class RandomizedSet:

    def __init__(self):
        self.hashset = {}
        self.listMap = []

    def insert(self, val: int) -> bool:
        if val not in self.hashset:
            self.hashset[val] = len(self.listMap)
            self.listMap.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.hashset:
            return False
        else:
            idxToRemoveInList = self.hashset[val]
            lastValueinList = self.listMap[-1]
            
            self.listMap[idxToRemoveInList] = lastValueinList
            self.listMap.pop()
            
            self.hashset[lastValueinList] = idxToRemoveInList
            del self.hashset[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.listMap)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()