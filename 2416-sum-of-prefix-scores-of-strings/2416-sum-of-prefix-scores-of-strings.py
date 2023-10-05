class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Trie:
    def __init__(self, words):
        self.trie = TrieNode()
        for word in words:
            self.insert(word)
        self.total = {}
    def insert(self, word):
        current = self.trie
        for i in word:
            current = current.children[i]
            current.count += 1
    def score(self, word):
        if word not in self.total:
            self.total[word] = 0
            current = self.trie
            for i in word:
                current = current.children[i]
                self.total[word] += current.count
        return self.total[word]

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:        
        wordTrie = Trie(words)
        return [wordTrie.score(word) for word in words]
        