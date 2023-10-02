class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, current):
            if i == len(word):
                return current.isEndOfWord
            letter = word[i]
            if letter == '.':
                for child in current.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if letter not in current.children:
                    return False
                return dfs(i + 1, current.children[letter])
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)