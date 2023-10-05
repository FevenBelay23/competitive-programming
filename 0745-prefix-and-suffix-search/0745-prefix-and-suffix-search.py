class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1

class WordFilter:

    def __init__(self , words: List[str]):
        self.trie = TrieNode()
        for idx, word in enumerate(words):
            self.insert(idx, word)
    
    def insert(self, idx, word):
        for i in range(len(word)-1, -2, -1):
            new = word[i+1:] + '#' + word
            current = self.trie
            current.idx = idx
            for letter in new:
                if letter not in current.children:
                    current.children[letter] = TrieNode()
                current = current.children[letter]
                current.idx = idx

    def f(self, pref: str, suff: str) -> int:
        current = self.trie
        new = suff + '#' + pref
        for letter in new:
            if letter not in current.children:
                return -1
            current = current.children[letter] 
        return current.idx
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)



