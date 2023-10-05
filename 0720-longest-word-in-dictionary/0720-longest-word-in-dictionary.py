
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            current = root
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = TrieNode()
                current = current.children[letter]
            current.isEndOfWord = True      
        longest_word = ''
        for word in words:
            if len(word) < len(longest_word):
                continue
            current = root
            for letter in word:
                current = current.children[letter]
                if not current.isEndOfWord:
                    break
            if current.isEndOfWord and (len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word)):
                longest_word = word                 
        return longest_word
       
        
