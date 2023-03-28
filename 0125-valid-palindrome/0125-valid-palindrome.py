class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = ""
        for letter in s.lower():
            if letter.isalnum():
                S += letter
        return S == S[::-1]
        