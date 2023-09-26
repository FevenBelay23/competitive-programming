class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a,2) + int(b,2)
        binary_string = bin(c)
        binary_string = binary_string[2:]
        return binary_string
        