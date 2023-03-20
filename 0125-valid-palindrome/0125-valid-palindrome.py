class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter for letter in s.lower() if letter.isalnum())
        return s == s[::-1]
        