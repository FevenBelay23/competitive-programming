class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        arrayDictionary = [float('inf')] * 26
        offset = ord('a')  
        for word in words:
            temp = [0] * 26
            for char in word:
                ascii_value = ord(char)
                temp[ascii_value - offset] += 1
            for i in range(26):
                arrayDictionary[i] = min(arrayDictionary[i], temp[i])
        for i in range(26):
            result.extend([chr(i + offset)] * arrayDictionary[i])
        return result