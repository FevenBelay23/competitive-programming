class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        s_count = [0] * 26
        output = []
 
        for j in p:
            p_count[ord(j) - ord('a')] += 1
   
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                s_count[ord(s[i-len(p)]) - ord('a')] -= 1
            if i >= len(p) - 1 and s_count == p_count:
                output.append(i - len(p) + 1)

        return output

        