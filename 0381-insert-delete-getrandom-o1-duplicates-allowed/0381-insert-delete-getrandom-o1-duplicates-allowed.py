from sortedcontainers import SortedList
class RandomizedCollection:

    def __init__(self):
        self.sl = SortedList()

    def insert(self, val: int) -> bool:
		# O(log N)
        boo = (val not in self.sl)
        self.sl.add(val)
        return boo

    def remove(self, val: int) -> bool:
		# O(log N)
        if val in self.sl:
            self.sl.remove(val) 
            return True
        return False

    def getRandom(self) -> int:
		# O(1)
         return random.choice(self.sl)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()