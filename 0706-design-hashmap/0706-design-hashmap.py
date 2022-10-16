class MyHashMap:

    def __init__(self):
        self.MAX_SIZE = 2069
        self.hashmap = [[] for _ in range(self.MAX_SIZE)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.MAX_SIZE
        found = False
        
        for idx, kv in enumerate(self.hashmap[hash_key]):
            if key == kv[0]:
                found = True
                self.hashmap[hash_key][idx] = (key, value)
                break
                
        if not found:
            self.hashmap[hash_key].append((key, value))

    def get(self, key: int) -> int:
        hash_key = key % self.MAX_SIZE
        found = False
        
        for idx, kv in enumerate(self.hashmap[hash_key]):
            if kv[0] == key:
                found = True
                return kv[1]
        
        if not found:
            return -1
        

    def remove(self, key: int) -> None:
        hash_key = key % self.MAX_SIZE
        
        for idx, kv in enumerate(self.hashmap[hash_key]):
            if key == kv[0]:
                del self.hashmap[hash_key][idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)