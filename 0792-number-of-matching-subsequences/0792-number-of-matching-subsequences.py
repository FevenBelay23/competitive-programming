class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = 0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter]=TrieNode()
            current=current.children[letter]
        current.isEndOfWord += 1
    
class Solution:
    def find(self,node,index):
        self.count += node.isEndOfWord
        if not node.children:
            return
        for letter,j in node.children.items():
            for i in range(index,len(self.s)):
                if self.s[i]==letter:
                    self.find(j,i+1)
                    break
        return
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.s = s
        self.count = 0
        self.find(trie.root,0)
        return self.count