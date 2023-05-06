class Solution:
    def maxProduct(self, words: List[str]) -> int:
        temp = {}
        for i in words:
            curr = 0
            for char in i:
                curr |= 1 << (ord(char) - ord('a'))
            temp[i] = curr
        max_value = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if temp[words[i]] & temp[words[j]] == 0:
                    max_value = max(max_value, len(words[i]) * len(words[j]))
        return max_value