class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(first,second):
           
            if not second and decreasing(first) and len(first) > 1:
                return True
            if not decreasing(first):
                return
           
            for i in range(len(second)):
                first.append(int(second[:i+1]))
                solved = backtrack(first,second[i+1:])
                if solved:
                    return True
                first.pop()
                
        def decreasing(first):
            for i in range(1, len(first)):
                if first[i-1] - 1 != first[i]:
                    return False
            return True
            
        # first = s[0:1]
        # second = s[1:]
        return backtrack([],s)
        