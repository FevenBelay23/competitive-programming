class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0 
        i, j = 0, 0
        while i < len(chars):
            count = 0
            current = chars[i]
            while i < len(chars) and chars[i] == current:
                i += 1
                count += 1
            chars[j] = current
            j += 1
            if count > 1:
                for k in str(count):
                    chars[j] = k
                    j += 1
        return j