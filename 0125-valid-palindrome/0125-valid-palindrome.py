class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = s.lower()
        pali = ""
        for i in phrase:
            if i.isalnum():
                pali+=i
        if pali == pali[::-1]:
            return True
        return False
        