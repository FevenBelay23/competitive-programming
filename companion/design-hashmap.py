class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.items = [None] * self.size

    def hashing(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        key_hash = self.hashing(key)
        if not self.items[key_hash]:
            self.items[key_hash] = []
        for i, (j, k) in enumerate(self.items[key_hash]):
            if j == key:
                self.items[key_hash][i] = (key, value)
                return
        self.items[key_hash].append((key, value))

    def get(self, key: int) -> int:
        key_hash = self.hashing(key)
        if not self.items[key_hash]:
            return -1
        for i, j in self.items[key_hash]:
            if i == key:
                return j
        return -1

    def remove(self, key: int) -> None:
        key_hash = self.hashing(key)
        if not self.items[key_hash]:
            return
        for i, (j, k) in enumerate(self.items[key_hash]):
            if j == key:
                del self.items[key_hash][i]
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)