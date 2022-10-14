class MyHashMap:

    def __init__(self):
        self.MAX_SIZE = 2069 # less collision
        self.hashmap = [ [] for _ in range(self.MAX_SIZE)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.MAX_SIZE
        
        found = False
        
        for idx, kv in enumerate(self.hashmap[hash_key]):
            if key == kv[0]:
                self.hashmap[hash_key][idx] = (key, value)
                found = True
                break
        
        if not found:
            self.hashmap[hash_key].append((key, value))

    def get(self, key: int) -> int:
        found = False
        hash_key = key % self.MAX_SIZE
        for kv in self.hashmap[hash_key]:
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

#                 class HashTable:  

        

    
#     def __getitem__(self, key):
#         arr_index = self.get_hash(key)
#         for kv in self.arr[arr_index]:
#             if kv[0] == key:
#                 return kv[1]
            
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[h]):
#             if len(element)==2 and element[0] == key:
#                 self.arr[h][idx] = (key,val)
#                 found = True
#         if not found:
#             self.arr[h].append((key,val))
        
#     def __delitem__(self, key):
#         arr_index = self.get_hash(key)
#         for index, kv in enumerate(self.arr[arr_index]):
#             if kv[0] == key:
#                 print("del",index)
#                 del self.arr[arr_index][index]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)