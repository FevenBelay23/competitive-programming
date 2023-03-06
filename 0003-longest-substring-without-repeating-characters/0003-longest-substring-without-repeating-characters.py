class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        current_length = max_length = 0
        index = {}

        for i in range(len(s)):
            if s[i] in index and index[s[i]] >= i - current_length:
                current_length = i - index[s[i]]
            else:
                current_length += 1
                
            index[s[i]] = i
            max_length = max(max_length, current_length)
 
        return max_length

        