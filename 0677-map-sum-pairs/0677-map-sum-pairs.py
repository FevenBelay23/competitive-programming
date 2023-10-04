class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False
        self.value=0
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map=defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:
        current = self.root
        for i in key:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
            current.value += val - self.map[key]
        current.isEndOfWord = True
        self.map[key]=val
            

    def sum(self, prefix: str) -> int:
        current=self.root
        for i in prefix:
            if i not in current.children:
                return 0
            current=current.children[i]
        return current.value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)