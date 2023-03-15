class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = '0'
        def reverse_invert(string):
            strr = ''
            for i in string:
                if i == '0':
                    strr = strr + '1'
                else:
                    strr = strr + '0'
            return strr[::-1]
        def kth(val):
            nonlocal ans
            if n == val:
                return 
            ans = ans + "1" + reverse_invert(ans)
            kth(val+1)
        kth(1)
        return ans[k-1]
        
