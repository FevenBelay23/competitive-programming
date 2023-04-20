class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        common_prefix = ""
        for i, letter in enumerate(strs[0]):
            for j in strs[1:]:
                if i >= len(j) or j[i] != letter:
                    return common_prefix
            common_prefix += letter
        return common_prefix