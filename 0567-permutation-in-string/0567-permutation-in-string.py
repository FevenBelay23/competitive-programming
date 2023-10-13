class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        freq = {}
        temp = {}
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        for i in range(n):
            char = s2[i]
            temp[char] = temp.get(char, 0) + 1
        for i in range(n, m):
            if freq == temp:
                return True
            left_char = s2[i - n]
            if temp[left_char] == 1:
                del temp[left_char]
            else:
                temp[left_char] -= 1
            new_char = s2[i]
            temp[new_char] = temp.get(new_char, 0) + 1
        return freq == temp