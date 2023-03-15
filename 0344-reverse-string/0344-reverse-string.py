class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        i=0
        j=len(s)-1
        def reverse(s,i,j):
            if i>=j:
                return
            s[i],s[j]=s[j],s[i]
            reverse(s,i+1,j-1)
        reverse(s,i,j)