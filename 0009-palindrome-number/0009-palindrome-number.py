class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to string
        x_str = str(x)

        # Check if the string is equal to its reverse
        return x_str == x_str[::-1]