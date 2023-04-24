class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(first, part):
            if first == len(s) and len(part) == 4:
                result.append(".".join(part))
                return
            if len(part) == 4:
                return
            for i in range(first, min(first+3, len(s))):
                if i > first and s[first] == "0":
                    return
                num = int(s[first:i+1])
                if num > 255:
                    return
                backtrack(i+1, part + [str(num)])

        result = []
        backtrack(0, [])
        return result