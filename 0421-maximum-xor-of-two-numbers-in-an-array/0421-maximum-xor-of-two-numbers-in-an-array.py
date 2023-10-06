class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        Length = len(bin(max(nums))) - 2 
        nums = [[(n >> i) & 1 for i in range(Length - 1, -1, -1)] for n in nums] 
        trie = {}
        max_xor = 0

        for i in nums:
            current = trie
            sp = trie
            val = 0
            for bit in i:
                if bit not in current:
                    current[bit] = {}
                current = current[bit]
                temp = 1 - bit
                val <<= 1
                if temp in sp:
                    sp = sp[temp]
                    val |= 1
                else:
                    sp = sp[bit]
            max_xor = max(max_xor, val)
        return max_xor