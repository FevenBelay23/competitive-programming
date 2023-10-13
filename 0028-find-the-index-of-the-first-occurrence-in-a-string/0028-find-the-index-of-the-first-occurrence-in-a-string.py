class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        chec = 101
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1  
        needle_hash = 0
        haystack_hash = 0
        for i in range(m):
            needle_hash = (needle_hash * 256 + ord(needle[i])) % chec
            haystack_hash = (haystack_hash * 256 + ord(haystack[i])) % chec
        for i in range(n - m + 1):
            if needle_hash == haystack_hash:
                if haystack[i:i + m] == needle:
                    return i
            if i < n - m:
                haystack_hash = (haystack_hash * 256 - ord(haystack[i]) * (256 ** m) + ord(haystack[i + m])) % chec
        return -1 
        